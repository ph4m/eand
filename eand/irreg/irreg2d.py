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

class Irreg2D:
    '''
    classdocs
    '''
    n1 = 0
    n2 = 0
    alpha1 = 0
    beta1 = 0
    alpha2 = 0
    beta2 = 0
    case = 0
    t1 = np.array([])
    t2 = np.array([])
    sortInd = []
    Ns = 0.
    G = np.array([[]])
    intEl = []
    intMap = [[]]
    delaunauTriangles = []
    delaunayCircumcenters = []
    t1Post = np.array([])
    t2Post = np.array([])
    ptToTri = [[]]
    sortInd = np.array([])

    def __init__(self,n1,n2,alpha1,beta1,alpha2,beta2,t1,t2,T1,T2):
        '''
        Constructor
        '''
        self.n1 = n1
        self.n2 = n2
        self.alpha1 = alpha1
        self.beta1 = beta1
        self.alpha2 = alpha2
        self.beta2 = beta2
        self.T1 = T1
        self.T2 = T2
        param = [n1,n2,alpha1,beta1,alpha2,beta2]
        n1Max = 2
        n2Max = 2
        alpha1Max = 0
        beta1Max = 0
        alpha2Max = 0
        beta2Max = 0
        paramPos = 1+ np.array([n1Max,n2Max,alpha1Max,beta1Max,alpha2Max,beta2Max])
        self.case = sum([param[i]*np.product(paramPos[(i+1):]) for i in range(len(param)-1)])
        # Make sure t1 and t2 are properly sorted
        (self.t1,self.t2) = self.sortInputs(t1, t2)
        self.Ns = len(t1)
        self.buildIntMap()
        self.initTriangles()
        

    
    def calcGxy(self,x,y,a,b,c,d):
        Gxy = ((b-x)**self.alpha1)*((a-x)**self.beta1)*((d-y)**self.alpha2)*((c-y)**self.beta2)
        if self.case == 5: # n1=alpha1=beta1=1,n2=alpha2=beta2=0
            partialGxy = a+b-2*x
        elif self.case == 2: # n1=alpha1=beta1=0,n2=alpha2=beta2=1
            partialGxy = c+d-2*y
        else:
            print '(n1=%d,n2=%d,alpha1=%d,beta1=%d,alpha2=%d,beta2=%d) not supported' % (self.n1,self.n2,self.alpha1,self.beta1,self.alpha2,self.beta2)
        return (Gxy,partialGxy)
    
    def calcGxyTranslated(self,x,y):
        Gxy = ((self.T1-x)**self.alpha1)*((-self.T1-x)**self.beta1)*((self.T2-y)**self.alpha2)*((-self.T2-y)**self.beta2)
        if self.case == 5: # n1=alpha1=beta1=1,n2=alpha2=beta2=0
            partialGxy = -2*x
        elif self.case == 2: # n1=alpha1=beta1=0,n2=alpha2=beta2=1
            partialGxy = -2*y
        else:
            print '(n1=%d,n2=%d,alpha1=%d,beta1=%d,alpha2=%d,beta2=%d) not supported' % (self.n1,self.n2,self.alpha1,self.beta1,self.alpha2,self.beta2)
        return (Gxy,partialGxy)
        
    def sortInputs(self,t1,t2,signal=[]):
        t1Sort = np.array(t1)
        self.sortInd = np.argsort(t1Sort)
        t1Sort = t1Sort[self.sortInd]
        t2Sort = np.array(t2)[self.sortInd]
        '''if len(signal) > 0:
            signalSort = np.array(signal)[sortInd]
        else:
            signalSort = []'''
        return (t1Sort,t2Sort)
    
    def sortSignal(self,signal):
        return np.array(signal)[self.sortInd]
        
    
    def differentiate(self,signal):
        dPost = []
        for i in self.intEl:
            processedTri = [0 for _ in range(len(self.delaunayTriangles))]
            dPostNum = 0.
            dPostDen = 0.
            for j in self.intMap[i]:
                for triLoc in self.ptToTri[j]:
                    if not processedTri[triLoc]:
                        processedTri[triLoc] = 1
                        pCirc = self.delaunayCircumcenters[triLoc]
                        if (pCirc[0] >= self.t1[i]-self.T1)*(pCirc[0] <= self.t1[i]+self.T1)*(pCirc[1] >= self.t2[i]-self.T2)*(pCirc[1] <= self.t2[i]+self.T2):
                            (p1,p2,p3) = self.delaunayTriangles[triLoc]
                            (Gxy1,partialGxy1) = self.calcGxyTranslated(self.t1[p1]-self.t1[i],self.t2[p1]-self.t2[i])
                            (Gxy2,partialGxy2) = self.calcGxyTranslated(self.t1[p2]-self.t1[i],self.t2[p2]-self.t2[i])
                            (Gxy3,partialGxy3) = self.calcGxyTranslated(self.t1[p3]-self.t1[i],self.t2[p3]-self.t2[i])
                            dPostNum = dPostNum + (partialGxy1*signal[p1]+partialGxy2*signal[p2]+partialGxy3*signal[p3])*self.triAreas[triLoc]#/3.
                            dPostDen = dPostDen + (Gxy1+Gxy2+Gxy3)*self.triAreas[triLoc]#/3.
            dPost.append(dPostNum/dPostDen)
        dPost = np.array(dPost)
        return (self.t1Post,self.t2Post,dPost)

    def buildIntMap(self):
        self.intMap = [[] for _ in range(self.Ns)]
        t1Min = min(self.t1)
        t1Max = max(self.t1)
        t2Min = min(self.t2)
        t2Max = max(self.t2)
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
            if (self.t2[i]-t2Min >= self.T2 and t2Max-self.t2[i] >= self.T2):
                intEl.append(i)
                while self.t1[i]-self.t1[iMinXLoc] > self.T1:
                    iMinXLoc += 1
                while self.t1[iMaxXLoc+1]-self.t1[i] < self.T1:
                    iMaxXLoc += 1
                for posPoint in range(iMinXLoc,iMaxXLoc+1):
                    if abs(self.t2[posPoint]-self.t2[i]) < self.T2:
                        self.intMap[i].append(posPoint)
        self.intEl = intEl
        self.t1Post = self.t1[intEl]
        self.t2Post = self.t2[intEl]

                        
    def plotDelaunay(self,plotNow=0):
        for t in self.delaunayTriangles:
            triLoc = [t[0], t[1], t[2], t[0]]
            plt.plot(self.t1[triLoc],self.t2[triLoc])
        plt.plot(self.t1,self.t2,'o')
        if plotNow:
            plt.show()

    def initTriangles(self):
        (self.delaunayCircumcenters, _, self.delaunayTriangles, _) = delaunay(self.t1,self.t2)
        nTri = len(self.delaunayTriangles)
        ptToTri = [[] for _ in range(self.Ns)]
        triAreas = [0. for _ in range(nTri)]
        for i in range(nTri):
            (p1,p2,p3) = self.delaunayTriangles[i]
            coord1 = np.array([self.t1[p1],self.t2[p1]])
            coord2 = np.array([self.t1[p2],self.t2[p2]])
            coord3 = np.array([self.t1[p3],self.t2[p3]])
            areaLoc = 0.5 * norm( np.cross( coord2-coord1, coord3-coord1 ) )
            ptToTri[p1].append(i)
            ptToTri[p2].append(i)
            ptToTri[p3].append(i)
            triAreas[i] = areaLoc
        self.ptToTri = ptToTri
        self.triAreas = triAreas
        
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
    
    def plotEstimate(self,t1Post,t2Post,dPost,waitPlot=0):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(t1Post,t2Post,dPost)
                
            
        