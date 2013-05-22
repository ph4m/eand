'''
eand.py package (Easy Algebraic Numerical Differentiation for Python)
Copyright (C) 2013 Tu-Hoa Pham

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

from matplotlib.delaunay import delaunay
import matplotlib.pyplot as plt
from numpy.linalg import norm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from derivativesgxy import DerivativesGxy

'''
Multidimensional derivative estimation with algebraic numerical differentiation
See 'Numerical differentiation on irregular grids' (Riachy et al., 2011)
'''
class IrrGridND:
    '''
    classdocs
    '''
    nDim = 0
    nParam = 0
    paramVec = [[]]
    case = 0
    tVec = []
    sortInd = []
    nSamples = 0.
    intPoints = []
    intMap = [[]]
    partitionCells = []
    partitionCenters = []
    tPost = []
    pointToCell = [[]]
    sortInd = np.array([])

    def __init__(self,paramVec,tVec):
        '''
        Constructor
        '''
        self.nDim = len(paramVec)
        self.paramVec = paramVec
        self.nVec = np.array([i[0] for i in paramVec])
        self.alphaVec = np.array([i[1] for i in paramVec])
        self.betaVec = np.array([i[2] for i in paramVec])
        self.halfWindowVec = np.array([i[3] for i in paramVec])
        self.case = self.calcCase()
        self.initCalcPartialGxy()
        self.tVec = self.sortAxis(tVec)
        self.nSamples = len(tVec[0])
        self.buildIntMap()
        self.initPartition()
        self.initCells()
    
    def calcCase(self):
        n1Max = 2
        alpha1Max = 4
        beta1Max = 4
        n2Max = 2
        alpha2Max = 4
        beta2Max = 4
        paramSeq = []
        for dim in range(self.nDim):
            paramSeq.append(self.nVec[dim])
            paramSeq.append(self.alphaVec[dim])
            paramSeq.append(self.betaVec[dim])
        if self.nDim == 1:
            for _ in range(3):
                paramSeq.append(0)
        paramPos = 1+ np.array([n1Max,alpha1Max,beta1Max,n2Max,alpha2Max,beta2Max])
        case = sum([paramSeq[i]*np.product(paramPos[(i+1):]) for i in range(len(paramSeq)-1)])+paramSeq[len(paramSeq)-1]
        return case
    
    def initCalcPartialGxy(self):
        try:
            derivativesGxy = DerivativesGxy(self.halfWindowVec,self.case)
            self.calcPartialGxy = derivativesGxy.partialGxy
        except:
            print 'ERROR:', 'parameter sequence', self.paramVec, 'is not supported'
            exit()
        
    
    def calcGxy1D(self,coord):
        Gxy = np.product([((self.halfWindowVec[dim]-coord[dim])**self.alphaVec[dim])*((-self.halfWindowVec[dim]-coord[dim])**self.betaVec[dim]) for dim in range(self.nDim)])
        if self.case == 12: # n1=alpha1=beta1=1
            partialGxy = -2*coord[0]
        else:
            print '(n1=%d,alpha1=%d,beta1=%d) not supported' % (self.nVec[0],self.alphaVec[0],self.betaVec[0])
        return (Gxy,partialGxy)
    
    def calcGxy2D(self,coord):
        Gxy = np.product([((self.halfWindowVec[dim]-coord[dim])**self.alphaVec[dim])*((-self.halfWindowVec[dim]-coord[dim])**self.betaVec[dim]) for dim in range(self.nDim)])
        if self.case == 351: # n1=alpha1=beta1=1,n2=alpha2=beta2=0
            partialGxy = -2*coord[0]
        elif self.case == 12: # n1=alpha1=beta1=0,n2=alpha2=beta2=1
            partialGxy = -2*coord[1]
        else:
            print '(n1=%d,alpha1=%d,beta1=%d,n2=%d,alpha2=%d,beta2=%d) not supported' % (self.nVec[0],self.alphaVec[0],self.betaVec[0],self.nVec[1],self.alphaVec[1],self.betaVec[1])
        return (Gxy,partialGxy)
        
    def sortAxis(self,tVec):
        tVecSorted = []
        self.sortInd = np.argsort(np.array(tVec[0]))
        for t in tVec:
            tVecSorted.append(np.array(t)[self.sortInd])
        return (np.array(tVecSorted))
    
    def sortSignal(self,signal):
        return np.array(signal)[self.sortInd]
    
    def isInWindow(self,coord):
        return np.product([(coord[dim] <= self.halfWindowVec[dim])*(coord[dim] >= -self.halfWindowVec[dim]) for dim in range(self.nDim)])
    
    
    
    def calcGxy(self,coord):
        return np.product([((self.halfWindowVec[dim]-coord[dim])**self.alphaVec[dim])*((-self.halfWindowVec[dim]-coord[dim])**self.betaVec[dim]) for dim in range(self.nDim)])
    
    def differentiate(self,signal):
        signalSorted = np.array(signal)[self.sortInd]
        dPost = []
        for i in self.intPoints:
            processedCells = [0 for _ in range(self.nCells)]
            dPostNum = 0.
            dPostDen = 0.
            for j in self.intMap[i]:
                for cell in self.pointToCell[j]:
                    if not processedCells[cell]:
                        processedCells[cell] = 1
                        coordRecentered = np.array(self.partitionCenters[cell]) - np.array([self.tVec[dim][i] for dim in range(self.nDim)])
                        if self.isInWindow(coordRecentered):
                            pVec = self.partitionCells[cell]
                            gxyVec = [self.calcGxy([self.tVec[dim][p]-self.tVec[dim][i] for dim in range(self.nDim)]) for p in pVec]
                            partialGxyVec = [self.calcPartialGxy([self.tVec[dim][p]-self.tVec[dim][i] for dim in range(self.nDim)]) for p in pVec]
                            dPostNum = dPostNum + np.dot(partialGxyVec,signalSorted[pVec])*self.cellVol[cell]
                            dPostDen = dPostDen + sum(gxyVec)*self.cellVol[cell]
            dPost.append(dPostNum/dPostDen)
        dPost = np.array(dPost)
        return (self.tPostVec,dPost)

    def buildIntMap(self):
        self.intMap = [[] for _ in range(self.nSamples)]
        tMinVec = [min(t) for t in self.tVec]
        tMaxVec = [max(t) for t in self.tVec]
        iMinFirstAxis = 0
        iMaxFirstAxis = self.nSamples-1
        while self.tVec[0][iMinFirstAxis]-tMinVec[0] < self.halfWindowVec[0]:
            iMinFirstAxis += 1
        while tMaxVec[0]-self.tVec[0][iMaxFirstAxis] < self.halfWindowVec[0]:
            iMaxFirstAxis -= 1
        intPoints = []
        iMinLoc = 0
        iMaxLoc = iMinFirstAxis
        for i in range(iMinFirstAxis,iMaxFirstAxis+1):
            if np.product([(self.tVec[dim][i]-tMinVec[dim] >= self.halfWindowVec[dim])*(tMaxVec[dim]-self.tVec[dim][i] >= self.halfWindowVec[dim]) for dim in range(1,self.nDim)]):
            #if (self.t2[i]-t2Min >= self.T2 and t2Max-self.t2[i] >= self.T2):
                intPoints.append(i)
                while self.tVec[0][i]-self.tVec[0][iMinLoc] > self.halfWindowVec[0]:
                    iMinLoc += 1
                while self.tVec[0][iMaxLoc+1]-self.tVec[0][i] < self.halfWindowVec[0]:
                    iMaxLoc += 1
                for testPoint in range(iMinLoc,iMaxLoc+1):
                    if np.product([abs(self.tVec[dim][testPoint]-self.tVec[dim][i])< self.halfWindowVec[dim] for dim in range(1,self.nDim)]):
                        self.intMap[i].append(testPoint)
        self.intPoints = intPoints
        self.tPostVec = [self.tVec[dim][intPoints] for dim in range(self.nDim)]

                        
    def plotPartition(self,plotNow=0):
        if self.nDim == 1:
            for cell in self.partitionCells:
                segment = [cell[0], cell[1]]
                plt.plot(self.tVec[0][segment],[0. for _ in self.tVec[0][segment]])
            plt.plot(self.tVec[0],[0. for _ in range(self.nSamples)],'o')
        elif self.nDim == 2:
            for cell in self.partitionCells:
                triangle = [cell[0], cell[1], cell[2], cell[0]]
                plt.plot(self.tVec[0][triangle],self.tVec[1][triangle])
            plt.plot(self.tVec[0],self.tVec[1],'o')
        if plotNow:
            plt.show()

    def initPartition(self):
        if self.nDim == 1:
            self.partitionCenters = []
            self.partitionCells = []
            for i in range(self.nSamples-1):
                self.partitionCenters.append([self.tVec[0][i],self.tVec[0][i+1]])
                self.partitionCells.append([i,i+1])
        elif self.nDim == 2:
            (self.partitionCenters, _, self.partitionCells, _) = delaunay(self.tVec[0],self.tVec[1])
        self.nCells = len(self.partitionCells)
    
    def calcVol(self,coordVec):
        if self.nDim == 1:
            return norm(coordVec[1]-coordVec[0])
        elif self.nDim == 2:
            return 0.5*norm(np.cross(coordVec[1]-coordVec[0],coordVec[2]-coordVec[0]))
    
    def initCells(self):
        pointToCell = [[] for _ in range(self.nSamples)]
        cellVol = [] #[0. for _ in range(self.nCells)]
        for i in range(self.nCells):
            pVec = self.partitionCells[i]
            coordVec = np.array([[self.tVec[dim][p] for dim in range(self.nDim)] for p in pVec])
            cellVol.append(self.calcVol(coordVec))
            for p in pVec:
                pointToCell[p].append(i)
        self.pointToCell = pointToCell
        self.cellVol = cellVol
        
    def plotSlice(self,tPostVec,dPost,coord,val,threshold,plotNow=0):
        if self.nDim == 1:
            self.plotScatter(tPostVec, dPost, plotNow)
            return (tPostVec[0],dPost)
        else:
            indSlice = []
            if coord == 1:
                for i in range(len(dPost)):
                    if abs(tPostVec[0][i]-val) < threshold:
                        indSlice.append(i)
                plt.figure()
                plt.scatter(tPostVec[1][indSlice],dPost[indSlice])
                return(tPostVec[1][indSlice],dPost[indSlice])
            elif coord == 2:
                for i in range(len(dPost)):
                    if abs(tPostVec[1][i]-val) < threshold:
                        indSlice.append(i)
                plt.figure()
                plt.scatter(tPostVec[0][indSlice],dPost[indSlice])
                return(tPostVec[0][indSlice],dPost[indSlice])
            else:
                'coordinate not supported'
            if plotNow:
                plt.show()
    
    def plotScatter(self,tPostVec,dPost,plotNow=0):
        if self.nDim == 1:
            plt.figure()
            plt.scatter(tPostVec[0],dPost)
        elif self.nDim == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(tPostVec[0],tPostVec[1],dPost)
        if plotNow:
            plt.show()
                
            
        