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
from scipy.misc import comb, factorial
from scipy import linalg

'''
Monodimensional derivative estimation with algebraic numerical differentiation
See 'Numerical differentiation with annihilators in noisy environments' (Mboup et al., 2009)
'''
class MonoDiff:
    '''
    Direct derivative estimation using a (kappa,mu)-algebraic numerical differentiator
    The differentiator is initialized based on the following parameters:
        n: the order at which derivative is to be estimated
        N: the truncation order of the local Taylor expansion
        kappa: estimation scaling parameter
        mu: estimation scaling parameter
        M: number of pointwise estimation samples used
        Ts: constant period between successive samples
        xi: parameter for estimation delay
        lambdaOptType: estimation error type to optimize ('mismodel' or 'noisyenv')
        causality: observation direction along time ('causal' or 'anticausal')
        flagCompleteTime: output completion into initial time sampling ('none', 'zero', 'findiff')
    From there, additional elements composing the differentiator can be computed:
        T: observation time for each estimate
        q: model complexity parameter
        lambdaElType: way vector lambda is calculated ('real', 'rational', 'constant')
        lambdaVec: vector lambda used for differentiator construction
        g: main vector characterizing the differentiator in FIR filter form
        W: vector of discreet integration weights
        delay: time delay of the differentiator
    Once constructed, the differentiator can then be applied on different signals
    '''
    n = 0
    N = 0
    kappa = 0
    mu = 0
    M = 0
    Ts = 0.
    xi = 0.
    lambdaOptType = ''
    causality = ''
    flagCompleteTime = 'zero'
    T = 0.
    q = 0
    lambdaElType = ''
    lambdaVec = np.array([])
    g = np.array([])
    W = np.array([])
    delay = 0.

    def __init__(self,cfg):
        '''
        Constructor
        '''
        # Initialize main parameters
        self.n = cfg['n']
        self.N = cfg['N']
        self.kappa = cfg['kappa']
        self.mu = cfg['mu']
        self.M = cfg['M']
        self.Ts = cfg['Ts']
        self.xi = cfg['xi']
        self.lambdaOptType = cfg['lambdaOptType']
        self.causality = cfg['causality']
        self.flagCompleteTime = cfg['flagCompleteTime']

        # Auxiliary parameters
        self.T = self.M*self.Ts
        self.q = self.N-self.n
        # initialization of vector lambda
        self.buildLambdaVec()
        # computation of h coefficients and construction of vector g
        self.buildGVec()
        # weight vector
        self.buildWVec()
        # calculate delay
        self.calcDelay()

    def differentiate(self,t,signal):
        '''
        Numerical differentiation method
        Once the differentiator is constructed, can be applied to compute derivative estimates
        Inputs:
            t: discreet observation time, regularly spaced
            signal: samples of the signal to differentiate
        Outputs:
            tPost: discreet estimation time after postprocessing
            dPost: derivative estimates
        '''
        Ns = len(t)
        dt = (t[Ns-1]-t[0])/Ns
        dEst = np.array([0. for _ in range(Ns)])
        lag = round(self.delay/self.Ts)
        if self.causality == 'causal':
            for l in range(self.M+1,Ns):
                for m in range(self.M+1):
                    dEst[l] = dEst[l] + self.W[m]*self.g[m]*signal[l-m]
            dPost = dEst[self.M:]
            dPost = dPost[lag:]
            tPost = t[self.M:]
            tPost = tPost[:len(dPost)]
        elif self.causality == 'anticausal':
            for l in range(Ns-self.M-1):
                for m in range(self.M+1):
                    dEst[l] = dEst[l] + self.W[m]*self.g[m]*signal[l+m]
            dPost = dEst[:Ns-self.M]
            dPost = dPost[:len(dPost)-lag]
            tPost = t[:Ns-self.M]
            tPost = tPost[len(tPost)-len(dPost):]
        # Complete tPost into t with finite difference
        if self.flagCompleteTime == 'zero' or self.flagCompleteTime == 'findiff':
            iCompleteBounds = [list(t).index(tPost[0]),list(t).index(tPost[len(tPost)-1])]
            tCompleteBegin = []
            dCompleteBegin = []
            tCompleteEnd = []
            dCompleteEnd = []
            if iCompleteBounds[0] > 0:
                tCompleteBegin = [t[i] for i in range(0,iCompleteBounds[0])]
                if self.flagCompleteTime == 'zero':
                    if self.n == 0:
                        valAverageBegin = np.mean([signal[i] for i in range(0,iCompleteBounds[0])])
                        for iComplete in range(0,iCompleteBounds[0]):
                            dCompleteBegin.append(valAverageBegin)
                    else:
                        for iComplete in range(0,iCompleteBounds[0]):
                            dCompleteBegin.append(0.0)
                elif self.flagCompleteTime == 'findiff':
                    if self.n == 0:
                        for iComplete in range(0,iCompleteBounds[0]):
                            dCompleteBegin.append(signal[iComplete])
                    elif self.n == 1:
                        dCompleteBegin.append((signal[1]-signal[0])/(dt))
                        for iComplete in range(1,iCompleteBounds[0]):
                            dCompleteBegin.append((signal[iComplete+1]-signal[iComplete-1])/(2*dt))
                    elif self.n == 2:
                        dCompleteBegin.append((signal[2]-2*signal[1]+signal[0])/(dt**2))
                        for iComplete in range(1,iCompleteBounds[0]):
                            dCompleteBegin.append((signal[iComplete+1]-2*signal[0]+signal[iComplete-1])/(dt**2))
                    else:
                        pass
            if iCompleteBounds[1] < Ns-1:
                tCompleteEnd = [t[i] for i in range(iCompleteBounds[1]+1,Ns)]
                if self.flagCompleteTime == 'zero':
                    if self.n == 0:
                        valAverageEnd = np.mean([signal[i] for i in range(iCompleteBounds[1]+1,Ns)])
                        for iComplete in range(iCompleteBounds[1]+1,Ns):
                            dCompleteEnd.append(valAverageEnd)
                    else:
                        for iComplete in range(iCompleteBounds[1]+1,Ns):
                            dCompleteEnd.append(0.0)
                elif self.flagCompleteTime == 'findiff':
                    if self.n == 0:
                        for iComplete in range(iCompleteBounds[1]+1,Ns):
                            dCompleteEnd.append(signal[iComplete])
                    elif self.n == 1:
                        for iComplete in range(iCompleteBounds[1]+1,Ns-1):
                            dCompleteEnd.append((signal[iComplete+1]-signal[iComplete-1])/(2*dt))
                        dCompleteEnd.append((signal[Ns-1]-signal[Ns-2])/(dt))
                    elif self.n == 2:
                        for iComplete in range(iCompleteBounds[1]+1,Ns-1):
                            dCompleteEnd.append((signal[iComplete+1]-2*signal[0]+signal[iComplete-1])/(dt**2))
                        dCompleteEnd.append((signal[Ns-1]-2*signal[Ns-2]+signal[Ns-3])/(dt**2))
                    else:
                        pass
            tPost = tCompleteBegin + list(tPost) + tCompleteEnd
            dPost = dCompleteBegin + list(dPost) + dCompleteEnd
        return (tPost,dPost)

    def calcDelay(self):
        '''
        Compute estimate time delay
        '''
        if (self.q == 0 or self.lambdaOptType == 'noisyenv'):
            xi1 = (self.kappa+self.n+1.)/(self.mu+self.kappa+2.*(self.n+1.));
            self.delay = self.T*xi1;
        elif (self.q <= self.kappa+self.n and self.lambdaOptType == 'mismodel'):
            self.delay = 0.
        else:
            self.delay = self.T*self.xi

    def buildWVec(self):
        '''
        Build vector of discreet integration weights
        Current method: trapezoidal method
        '''
        W = np.array([1./self.M for _ in range(self.M+1)])
        W[0] = 1./(2*self.M)
        W[self.M] = 1./(2*self.M)
        self.W = W

    def buildGVec(self):
        '''
        Main vector characterizing the differentiator in FIR filter form
        '''
        g = np.array([0.]*(self.M+1))
        for m in range(self.M+1):
            tau = m*self.Ts/self.T
            h = np.array([0.]*(self.q+1))
            for l in range(self.q+1):
                h[l] = self.calcHkm(tau,self.kappa+self.q-l,self.mu+l,self.n,self.T,self.causality);
            g[m] = sum(self.lambdaVec*h)
        self.g = g

    def buildLambdaVec(self):
        '''
        Build vector lambda according to estimation parameters and error source to minimize
        '''
        if self.lambdaOptType == 'mismodel':
            if self.q <= self.kappa+self.n:
                self.lambdaElType = 'rational'
            else:
                self.lambdaElType = 'real'
        elif self.lambdaOptType == 'noisyenv':
            self.lambdaElType = 'constant'
        else:
            print self.lambdaOptType, 'not recognized'
        if self.lambdaElType == 'real':
            b = np.array([0.]*(self.q+1))
            for l in range(self.q+1):
                b[l] = self.calcBlq(self.xi,l,self.q)
            A = np.array([[0. for _ in range(self.q+1)] for _ in range(self.q+1)])
            for i in range(self.q+1):
                for j in range(self.q+1):
                    A[i][j] = comb(self.mu+self.n+i+j,self.mu+self.n+j)*comb(self.kappa+self.n+2*self.q-(i+j),self.kappa+self.n+self.q-j)/comb(self.mu+self.kappa+2*self.n+2*self.q+1,self.q);
            lambdaVec = linalg.inv(A)*b
        elif self.lambdaElType == 'rational':
            p = self.n+self.kappa
            lambdaVec = np.array([0]*(self.q+1))
            for j in range(self.q+1):
                if self.q <= p:
                    m = 0
                else:
                    m = max(0,j-p)
                for i in range(m,j+1):
                    lambdaVec[j] = lambdaVec[j] + self.calcAij(i,j,p,self.q)
                lambdaVec[j] = (-1)**(self.q-j)*factorial(self.n+self.kappa+self.q-j)/(factorial(p)*factorial(self.q))*lambdaVec[j]
        elif self.lambdaElType == 'constant':
            lambdaVec = np.array([1./(self.q+1) for _ in range(self.q+1)])
        else:
            print self.lambdaElType, 'not recognized'
        self.lambdaVec = lambdaVec

    def calcAif(self,i,j,p,q):
        '''
        Compute aij coefficients
        '''
        aij = comb(q,i)*comb(p,j-i)*factorial(q+1)/((q+1-i)*factorial(q-j))
        return aij

    def calcBlq(self,tau,l,q):
        '''
        Compute blq coefficients
        '''
        blq = comb(q,l)*tau**(q-l)*(1-tau)**l
        return blq

    def calcHkm(self,tau,kappa,mu,n,T,causality):
        '''
        Compute hkm coefficients
        '''
        hkm = self.calcGamma(kappa,mu,n)/(T**n)*((tau >= 0) and (tau <= 1))*self.calcDnw(tau,kappa,mu,n);
        if causality == 'anticausal':
            hkm = (-1)**n*hkm
        return hkm

    def calcGamma(self,kappa,mu,n):
        '''
        Compute gamma coefficients
        '''
        gamma = factorial(mu+kappa+2*n+1)/(factorial(mu+n)*factorial(kappa+n))
        return gamma

    def calcDnw(self,t,kappa,mu,n):
        '''
        Compute exact derivatives of the Jacobi polynomials weight function
        '''
        # Supported parameters
        kappaMax = 6;
        muMax = 6;
        nMax = 2;

        # Index of the weight function derivative
        case = kappa*(muMax+1)*(nMax+1) + mu*(nMax+1) + n + 1;

        # Find the corresponding exact derivative
        if case > (kappaMax+1)*(muMax+1)*(nMax+1):
            print kappa, mu, n, 'combination not supported'
        else:
            if case == 1: res = 1
            elif case == 2: res = 1 - 2*t
            elif case == 3: res = 2*(1 - t)**2 - 8*(1 - t)*t + 2*t**2
            elif case == 4: res = 1 - t
            elif case == 5: res = (1 - t)**2 - 2*(1 - t)*t
            elif case == 6: res = 2*(1 - t)**3 - 12*(1 - t)**2*t + 6*(1 - t)*t**2
            elif case == 7: res = (1 - t)**2
            elif case == 8: res = (1 - t)**3 - 3*(1 - t)**2*t
            elif case == 9: res = 2*(1 - t)**4 - 16*(1 - t)**3*t + 12*(1 - t)**2*t**2
            elif case == 10: res = (1 - t)**3
            elif case == 11: res = (1 - t)**4 - 4*(1 - t)**3*t
            elif case == 12: res = 2*(1 - t)**5 - 20*(1 - t)**4*t + 20*(1 - t)**3*t**2
            elif case == 13: res = (1 - t)**4
            elif case == 14: res = (1 - t)**5 - 5*(1 - t)**4*t
            elif case == 15: res = 2*(1 - t)**6 - 24*(1 - t)**5*t + 30*(1 - t)**4*t**2
            elif case == 16: res = (1 - t)**5
            elif case == 17: res = (1 - t)**6 - 6*(1 - t)**5*t
            elif case == 18: res = 2*(1 - t)**7 - 28*(1 - t)**6*t + 42*(1 - t)**5*t**2
            elif case == 19: res = (1 - t)**6
            elif case == 20: res = (1 - t)**7 - 7*(1 - t)**6*t
            elif case == 21: res = 2*(1 - t)**8 - 32*(1 - t)**7*t + 56*(1 - t)**6*t**2
            elif case == 22: res = t
            elif case == 23: res = 2*(1 - t)*t - t**2
            elif case == 24: res = 6*(1 - t)**2*t - 12*(1 - t)*t**2 + 2*t**3
            elif case == 25: res = (1 - t)*t
            elif case == 26: res = 2*(1 - t)**2*t - 2*(1 - t)*t**2
            elif case == 27: res = 6*(1 - t)**3*t - 18*(1 - t)**2*t**2 + 6*(1 - t)*t**3
            elif case == 28: res = (1 - t)**2*t
            elif case == 29: res = 2*(1 - t)**3*t - 3*(1 - t)**2*t**2
            elif case == 30: res = 6*(1 - t)**4*t - 24*(1 - t)**3*t**2 + 12*(1 - t)**2*t**3
            elif case == 31: res = (1 - t)**3*t
            elif case == 32: res = 2*(1 - t)**4*t - 4*(1 - t)**3*t**2
            elif case == 33: res = 6*(1 - t)**5*t - 30*(1 - t)**4*t**2 + 20*(1 - t)**3*t**3
            elif case == 34: res = (1 - t)**4*t
            elif case == 35: res = 2*(1 - t)**5*t - 5*(1 - t)**4*t**2
            elif case == 36: res = 6*(1 - t)**6*t - 36*(1 - t)**5*t**2 + 30*(1 - t)**4*t**3
            elif case == 37: res = (1 - t)**5*t
            elif case == 38: res = 2*(1 - t)**6*t - 6*(1 - t)**5*t**2
            elif case == 39: res = 6*(1 - t)**7*t - 42*(1 - t)**6*t**2 + 42*(1 - t)**5*t**3
            elif case == 40: res = (1 - t)**6*t
            elif case == 41: res = 2*(1 - t)**7*t - 7*(1 - t)**6*t**2
            elif case == 42: res = 6*(1 - t)**8*t - 48*(1 - t)**7*t**2 + 56*(1 - t)**6*t**3
            elif case == 43: res = t**2
            elif case == 44: res = 3*(1 - t)*t**2 - t**3
            elif case == 45: res = 12*(1 - t)**2*t**2 - 16*(1 - t)*t**3 + 2*t**4
            elif case == 46: res = (1 - t)*t**2
            elif case == 47: res = 3*(1 - t)**2*t**2 - 2*(1 - t)*t**3
            elif case == 48: res = 12*(1 - t)**3*t**2 - 24*(1 - t)**2*t**3 + 6*(1 - t)*t**4
            elif case == 49: res = (1 - t)**2*t**2
            elif case == 50: res = 3*(1 - t)**3*t**2 - 3*(1 - t)**2*t**3
            elif case == 51: res = 12*(1 - t)**4*t**2 - 32*(1 - t)**3*t**3 + 12*(1 - t)**2*t**4
            elif case == 52: res = (1 - t)**3*t**2
            elif case == 53: res = 3*(1 - t)**4*t**2 - 4*(1 - t)**3*t**3
            elif case == 54: res = 12*(1 - t)**5*t**2 - 40*(1 - t)**4*t**3 + 20*(1 - t)**3*t**4
            elif case == 55: res = (1 - t)**4*t**2
            elif case == 56: res = 3*(1 - t)**5*t**2 - 5*(1 - t)**4*t**3
            elif case == 57: res = 12*(1 - t)**6*t**2 - 48*(1 - t)**5*t**3 + 30*(1 - t)**4*t**4
            elif case == 58: res = (1 - t)**5*t**2
            elif case == 59: res = 3*(1 - t)**6*t**2 - 6*(1 - t)**5*t**3
            elif case == 60: res = 12*(1 - t)**7*t**2 - 56*(1 - t)**6*t**3 + 42*(1 - t)**5*t**4
            elif case == 61: res = (1 - t)**6*t**2
            elif case == 62: res = 3*(1 - t)**7*t**2 - 7*(1 - t)**6*t**3
            elif case == 63: res = 12*(1 - t)**8*t**2 - 64*(1 - t)**7*t**3 + 56*(1 - t)**6*t**4
            elif case == 64: res = t**3
            elif case == 65: res = 4*(1 - t)*t**3 - t**4
            elif case == 66: res = 20*(1 - t)**2*t**3 - 20*(1 - t)*t**4 + 2*t**5
            elif case == 67: res = (1 - t)*t**3
            elif case == 68: res = 4*(1 - t)**2*t**3 - 2*(1 - t)*t**4
            elif case == 69: res = 20*(1 - t)**3*t**3 - 30*(1 - t)**2*t**4 + 6*(1 - t)*t**5
            elif case == 70: res = (1 - t)**2*t**3
            elif case == 71: res = 4*(1 - t)**3*t**3 - 3*(1 - t)**2*t**4
            elif case == 72: res = 20*(1 - t)**4*t**3 - 40*(1 - t)**3*t**4 + 12*(1 - t)**2*t**5
            elif case == 73: res = (1 - t)**3*t**3
            elif case == 74: res = 4*(1 - t)**4*t**3 - 4*(1 - t)**3*t**4
            elif case == 75: res = 20*(1 - t)**5*t**3 - 50*(1 - t)**4*t**4 + 20*(1 - t)**3*t**5
            elif case == 76: res = (1 - t)**4*t**3
            elif case == 77: res = 4*(1 - t)**5*t**3 - 5*(1 - t)**4*t**4
            elif case == 78: res = 20*(1 - t)**6*t**3 - 60*(1 - t)**5*t**4 + 30*(1 - t)**4*t**5
            elif case == 79: res = (1 - t)**5*t**3
            elif case == 80: res = 4*(1 - t)**6*t**3 - 6*(1 - t)**5*t**4
            elif case == 81: res = 20*(1 - t)**7*t**3 - 70*(1 - t)**6*t**4 + 42*(1 - t)**5*t**5
            elif case == 82: res = (1 - t)**6*t**3
            elif case == 83: res = 4*(1 - t)**7*t**3 - 7*(1 - t)**6*t**4
            elif case == 84: res = 20*(1 - t)**8*t**3 - 80*(1 - t)**7*t**4 + 56*(1 - t)**6*t**5
            elif case == 85: res = t**4
            elif case == 86: res = 5*(1 - t)*t**4 - t**5
            elif case == 87: res = 30*(1 - t)**2*t**4 - 24*(1 - t)*t**5 + 2*t**6
            elif case == 88: res = (1 - t)*t**4
            elif case == 89: res = 5*(1 - t)**2*t**4 - 2*(1 - t)*t**5
            elif case == 90: res = 30*(1 - t)**3*t**4 - 36*(1 - t)**2*t**5 + 6*(1 - t)*t**6
            elif case == 91: res = (1 - t)**2*t**4
            elif case == 92: res = 5*(1 - t)**3*t**4 - 3*(1 - t)**2*t**5
            elif case == 93: res = 30*(1 - t)**4*t**4 - 48*(1 - t)**3*t**5 + 12*(1 - t)**2*t**6
            elif case == 94: res = (1 - t)**3*t**4
            elif case == 95: res = 5*(1 - t)**4*t**4 - 4*(1 - t)**3*t**5
            elif case == 96: res = 30*(1 - t)**5*t**4 - 60*(1 - t)**4*t**5 + 20*(1 - t)**3*t**6
            elif case == 97: res = (1 - t)**4*t**4
            elif case == 98: res = 5*(1 - t)**5*t**4 - 5*(1 - t)**4*t**5
            elif case == 99: res = 30*(1 - t)**6*t**4 - 72*(1 - t)**5*t**5 + 30*(1 - t)**4*t**6
            elif case == 100: res = (1 - t)**5*t**4
            elif case == 101: res = 5*(1 - t)**6*t**4 - 6*(1 - t)**5*t**5
            elif case == 102: res = 30*(1 - t)**7*t**4 - 84*(1 - t)**6*t**5 + 42*(1 - t)**5*t**6
            elif case == 103: res = (1 - t)**6*t**4
            elif case == 104: res = 5*(1 - t)**7*t**4 - 7*(1 - t)**6*t**5
            elif case == 105: res = 30*(1 - t)**8*t**4 - 96*(1 - t)**7*t**5 + 56*(1 - t)**6*t**6
            elif case == 106: res = t**5
            elif case == 107: res = 6*(1 - t)*t**5 - t**6
            elif case == 108: res = 42*(1 - t)**2*t**5 - 28*(1 - t)*t**6 + 2*t**7
            elif case == 109: res = (1 - t)*t**5
            elif case == 110: res = 6*(1 - t)**2*t**5 - 2*(1 - t)*t**6
            elif case == 111: res = 42*(1 - t)**3*t**5 - 42*(1 - t)**2*t**6 + 6*(1 - t)*t**7
            elif case == 112: res = (1 - t)**2*t**5
            elif case == 113: res = 6*(1 - t)**3*t**5 - 3*(1 - t)**2*t**6
            elif case == 114: res = 42*(1 - t)**4*t**5 - 56*(1 - t)**3*t**6 + 12*(1 - t)**2*t**7
            elif case == 115: res = (1 - t)**3*t**5
            elif case == 116: res = 6*(1 - t)**4*t**5 - 4*(1 - t)**3*t**6
            elif case == 117: res = 42*(1 - t)**5*t**5 - 70*(1 - t)**4*t**6 + 20*(1 - t)**3*t**7
            elif case == 118: res = (1 - t)**4*t**5
            elif case == 119: res = 6*(1 - t)**5*t**5 - 5*(1 - t)**4*t**6
            elif case == 120: res = 42*(1 - t)**6*t**5 - 84*(1 - t)**5*t**6 + 30*(1 - t)**4*t**7
            elif case == 121: res = (1 - t)**5*t**5
            elif case == 122: res = 6*(1 - t)**6*t**5 - 6*(1 - t)**5*t**6
            elif case == 123: res = 42*(1 - t)**7*t**5 - 98*(1 - t)**6*t**6 + 42*(1 - t)**5*t**7
            elif case == 124: res = (1 - t)**6*t**5
            elif case == 125: res = 6*(1 - t)**7*t**5 - 7*(1 - t)**6*t**6
            elif case == 126: res = 42*(1 - t)**8*t**5 - 112*(1 - t)**7*t**6 + 56*(1 - t)**6*t**7
            elif case == 127: res = t**6
            elif case == 128: res = 7*(1 - t)*t**6 - t**7
            elif case == 129: res = 56*(1 - t)**2*t**6 - 32*(1 - t)*t**7 + 2*t**8
            elif case == 130: res = (1 - t)*t**6
            elif case == 131: res = 7*(1 - t)**2*t**6 - 2*(1 - t)*t**7
            elif case == 132: res = 56*(1 - t)**3*t**6 - 48*(1 - t)**2*t**7 + 6*(1 - t)*t**8
            elif case == 133: res = (1 - t)**2*t**6
            elif case == 134: res = 7*(1 - t)**3*t**6 - 3*(1 - t)**2*t**7
            elif case == 135: res = 56*(1 - t)**4*t**6 - 64*(1 - t)**3*t**7 + 12*(1 - t)**2*t**8
            elif case == 136: res = (1 - t)**3*t**6
            elif case == 137: res = 7*(1 - t)**4*t**6 - 4*(1 - t)**3*t**7
            elif case == 138: res = 56*(1 - t)**5*t**6 - 80*(1 - t)**4*t**7 + 20*(1 - t)**3*t**8
            elif case == 139: res = (1 - t)**4*t**6
            elif case == 140: res = 7*(1 - t)**5*t**6 - 5*(1 - t)**4*t**7
            elif case == 141: res = 56*(1 - t)**6*t**6 - 96*(1 - t)**5*t**7 + 30*(1 - t)**4*t**8
            elif case == 142: res = (1 - t)**5*t**6
            elif case == 143: res = 7*(1 - t)**6*t**6 - 6*(1 - t)**5*t**7
            elif case == 144: res = 56*(1 - t)**7*t**6 - 112*(1 - t)**6*t**7 + 42*(1 - t)**5*t**8
            elif case == 145: res = (1 - t)**6*t**6
            elif case == 146: res = 7*(1 - t)**7*t**6 - 7*(1 - t)**6*t**7
            elif case == 147: res = 56*(1 - t)**8*t**6 - 128*(1 - t)**7*t**7 + 56*(1 - t)**6*t**8
        return res
