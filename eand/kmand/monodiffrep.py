'''
eand package (Easy Algebraic Numerical Differentiation)
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

import numpy as np
#from eand.kmand.monodiff import MonoDiff
from monodiff import MonoDiff

'''
Derivative estimation through repeated (kappa,mu)-algebraic numerical differentiation
See 'Numerical differentiation with annihilators in noisy environments' (Mboup et al., 2009)
@author: Tu-Hoa Pham
'''
class MonoDiffRep:
    '''
    Derivative estimation through repeated (kappa,mu)-algebraic numerical differentiation
    The differentiator is initialized based on the following parameters:
        nTarget: the order at which derivative is to be estimated
        qVec: list of model complexity parameters for order 0 to nTarget
        kappaVec: list of estimation scaling parameters for order 0 to nTarget
        muVec: list of estimation scaling parameters for order 0 to nTarget
        MVec: list of numbers of pointwise estimation samples for order 0 to nTarget
        Ts: constant period between successive samples
        xi: parameter for estimation delay
        lambdaOptType: estimation error type to optimize ('mismodel' or 'noisyenv')
        causality: observation direction along time ('causal' or 'anticausal')
        rediffSeq: list of estimates to use for redifferentiation, -1 if initial signal
    From there, additional elements composing the differentiator can be computed:
        TVec: observation times for each estimate for order 0 to nTarget
        nVec: list of derivative orders to estimate
        NVec: list of Taylor expansion orders for order 0 to nTarget
        lambdaElType: way vector lambda is calculated ('real', 'rational', 'constant')
        lambdaVec: vector lambda used for differentiator construction
        differentiators: list of successive differentiators for order 0 to nTarget
    Once constructed, the differentiator can then be applied on different signals
    '''

    nTarget = 0
    qVec = []
    kappaVec = []
    muVec = []
    MVec = []
    Ts = 0.
    xi = 0.
    lambdaOptType = ''
    causality = ''
    flagCompleteTime = 'zero'
    rediffSeq = []
    TVec = []
    nVec = []
    NVec = []
    lambdaElType = ''
    lambdaVec = np.array([])
    differentiators = []

    def __init__(self,nTarget,qVec,kappaVec,muVec,MVec,Ts,xi,lambdaOptType,causality,flagCompleteTime,rediffSeq):
        '''
        Constructor
        '''
        # Initialize main parameters
        self.nTarget = nTarget
        self.qVec = np.array(qVec)
        self.kappaVec = np.array(kappaVec)
        self.muVec = np.array(muVec)
        self.MVec = np.array(MVec)
        self.Ts = Ts
        self.lambdaOptType = lambdaOptType
        self.xi = xi
        self.causality = causality
        self.flagCompleteTime = flagCompleteTime
        self.TVec = self.MVec*Ts
        self.nVec = [i-max(rediffSeq[i],0) for i in range(nTarget+1)]
        self.NVec = self.nVec+self.qVec
        self.rediffSeq = rediffSeq
        self.differentiators = []
        # Construct successive differentiators
        self.buildDifferentiators()
        
    def buildDifferentiators(self):
        '''
        Construct successive differentiators
        '''
        for order in range(self.nTarget+1):
            n = self.nVec[order]
            N = self.NVec[order]
            kappa = self.kappaVec[order]
            mu = self.muVec[order]
            M = self.MVec[order]
            diffLoc = MonoDiff(n,N,kappa,mu,M,self.Ts,self.xi,self.lambdaOptType,self.causality,self.flagCompleteTime)
            self.differentiators.append(diffLoc)
    
    def differentiate(self,t,signal):
        '''
        Numerical differentiation method
        Once the differentiator is constructed, can be applied to compute derivative estimates
        Inputs:
            t: discreet observation time, regularly spaced
            signal: samples of the signal to differentiate
        Outputs:
            tPostVec: list of discreet estimation times after postprocessing for order 0 to nTarget
            dPostVec: list of derivative estimates for order 0 to nTarget
        '''
        dPostSeq = []
        tPostSeq = []
        for n in range(self.nTarget+1):
            if self.rediffSeq[n] == -1:
                signalLoc = signal
                tLoc = t
            else:
                signalLoc = dPostSeq[self.rediffSeq[n]]
                tLoc = tPostSeq[self.rediffSeq[n]]
            (tPost,dPost) = self.differentiators[n].differentiate(tLoc,signalLoc)
            tPostSeq.append(tPost)
            dPostSeq.append(dPost)
        return (tPostSeq,dPostSeq)
            
