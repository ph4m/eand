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

class Irreg1D:
    '''
    classdocs
    '''
    n1 = 0
    alpha1 = 0
    beta1 = 0
    case = 0
    t1 = np.array([])
    sortInd = []
    Ns = 0.
    G = np.array([[]])
    intEl = []
    intMap = [[]]
    partitionCenters = []
    partitionSegments = []
    t1Post = np.array([])
    ptToSeg = [[]]
    sortInd = np.array([])

    def __init__(self,n1,alpha1,beta1,t1,T1):
        '''
        Constructor
        '''
        self.n1 = n1
        self.alpha1 = alpha1
        self.beta1 = beta1
        self.T1 = T1
        param = [n1,alpha1,beta1]
        n1Max = 2
        alpha1Max = 2
        beta1Max = 2
        paramPos = 1+ np.array([n1Max,alpha1Max,beta1Max])
        self.case = sum([param[i]*np.product(paramPos[(i+1):]) for i in range(len(param)-1)])
        # Make sure t1 and t2 are properly sorted
        (self.t1) = self.sortInputs(t1)
        self.Ns = len(t1)
        self.buildIntMap()
        self.initSegments()
    
    def calcGxy(self,x,y,a,b):
        Gxy = ((b-x)**self.alpha1)*((a-x)**self.beta1)
        if self.case == 12: # n1=alpha1=beta1=1
            partialGxy = a+b-2*x
        else:
            print '(n1=%d,n2=%d,alpha1=%d,beta1=%d,alpha2=%d,beta2=%d) not supported' % (self.n1,self.n2,self.alpha1,self.beta1,self.alpha2,self.beta2)
        return (Gxy,partialGxy)
    
    def calcGxyTranslated(self,x):
        Gxy = ((self.T1-x)**self.alpha1)*((-self.T1-x)**self.beta1)
        if self.case == 12: # n1=alpha1=beta1=1
            partialGxy = -2*x
        else:
            print '(n1=%d,n2=%d,alpha1=%d,beta1=%d,alpha2=%d,beta2=%d) not supported' % (self.n1,self.n2,self.alpha1,self.beta1,self.alpha2,self.beta2)
        return (Gxy,partialGxy)
        
    def sortInputs(self,t1,signal=[]):
        t1Sort = np.array(t1)
        self.sortInd = np.argsort(t1Sort)
        t1Sort = t1Sort[self.sortInd]
        return (t1Sort)
    
    def sortSignal(self,signal):
        return np.array(signal)[self.sortInd]
        
    
    def differentiate(self,signal):
        dPost = []
        for i in self.intEl:
            processedSeg = [0 for _ in range(len(self.partitionSegments))]
            dPostNum = 0.
            dPostDen = 0.
            for j in self.intMap[i]:
                for segLoc in self.ptToSeg[j]:
                    if not processedSeg[segLoc]:
                        processedSeg[segLoc] = 1
                        pCenter = self.partitionCenters[segLoc]
                        if (pCenter[0] >= self.t1[i]-self.T1)*(pCenter[0] <= self.t1[i]+self.T1):
                            (p1,p2) = self.partitionSegments[segLoc]
                            (Gxy1,partialGxy1) = self.calcGxyTranslated(self.t1[p1]-self.t1[i])
                            (Gxy2,partialGxy2) = self.calcGxyTranslated(self.t1[p2]-self.t1[i])
                            dPostNum = dPostNum + (partialGxy1*signal[p1]+partialGxy2*signal[p2])*self.segLen[segLoc]#/2.
                            dPostDen = dPostDen + (Gxy1+Gxy2)*self.segLen[segLoc]#/2.
            dPost.append(dPostNum/dPostDen)
        dPost = np.array(dPost)
        return (self.t1Post,dPost)

    def buildIntMap(self):
        self.intMap = [[] for _ in range(self.Ns)]
        t1Min = min(self.t1)
        t1Max = max(self.t1)
        iMinX = 0
        iMaxX = self.Ns-1
        while self.t1[iMinX]-t1Min < self.T1:
            iMinX += 1
        while t1Max-self.t1[iMaxX] < self.T1:
            iMaxX -= 1
        intEl = []
        iMinXLoc = 0
        iMaxXLoc = iMinX
        for i in range(iMinX,iMaxX+1):
            intEl.append(i)
            while self.t1[i]-self.t1[iMinXLoc] > self.T1:
                iMinXLoc += 1
            while self.t1[iMaxXLoc+1]-self.t1[i] < self.T1:
                iMaxXLoc += 1
            for posPoint in range(iMinXLoc,iMaxXLoc+1):
                self.intMap[i].append(posPoint)
        self.intEl = intEl
        self.t1Post = self.t1[intEl]


    def plotPartition(self,plotNow=0):
        for t in self.partitionSegments:
            segLoc = [t[0], t[1]]
            plt.plot(self.t1[segLoc],[0. for _ in self.t1[segLoc]])
        plt.plot(self.t1,[0. for _ in self.t1],'o')
        if plotNow:
            plt.show()


    def initSegments(self):
        self.partitionCenters = []#np.array([np.array([]) for _ in range(self.Ns)])
        self.partitionSegments = []#np.array([np.array([]) for _ in range(self.Ns)])
        for i in range(self.Ns-1):
            #self.partitionCenters.append(np.array([self.t1[i],self.t1[i+1]]))
            #self.partitionSegments.append(np.array([i,i+1]))
            self.partitionCenters.append([self.t1[i],self.t1[i+1]])
            self.partitionSegments.append([i,i+1])
        nSeg = len(self.partitionSegments)
        ptToSeg = [[] for _ in range(self.Ns)]
        segLen = [0. for _ in range(nSeg)]
        for i in range(nSeg):
            (p1,p2) = self.partitionSegments[i]
            coord1 = np.array([self.t1[p1]])
            coord2 = np.array([self.t1[p2]])
            segLenLoc = norm(coord2-coord1)
            ptToSeg[p1].append(i)
            ptToSeg[p2].append(i)
            segLen[i] = segLenLoc
        self.ptToSeg = ptToSeg
        self.segLen = segLen
    '''
    def plotSlice(self,t1Post,t2Post,dPost,coord,val,threshold,plotNow=0):
        indSlice = []
        if coord == 't1':
            for i in range(len(t1Post)):
                if abs(t1Post[i]-val) < threshold:
                    indSlice.append(i)
            plt.figure()
            plt.scatter(t2Post[indSlice],dPost[indSlice])
            return(t2Post[indSlice],dPost[indSlice])
        elif coord == 't2':
            for i in range(len(t2Post)):
                if abs(t2Post[i]-val) < threshold:
                    indSlice.append(i)
            plt.figure()
            plt.scatter(t1Post[indSlice],dPost[indSlice])
            return(t1Post[indSlice],dPost[indSlice])
        else:
            'coordinate not supported'
        if plotNow:
            plt.show()
    '''
    
    def plotScatter(self,t1Post,dPost,waitPlot=0):
        plt.figure()
        plt.scatter(t1Post,dPost)
                
            
        