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

from eand.mddig.multidiff import MultiDiff

'''
Multidimensional derivative estimation with repeated algebraic numerical differentiation
See 'Numerical differentiation on irregular grids' (Riachy et al., 2011)
'''
class MultiDiffRep:
    '''
    Multidimensional derivative estimation on irregular grids
    The differentiator is initialized based on the following parameters:
        paramVecSeq: list of paramVec vectors for differentiation step 1 to nDiffStep
        tVec: list of original sampling coordinates
    Additional attributes are:
        nDiffStep: number of differentiation steps
        differentiators: list of successive differentiators for step 1 to nDiffStep
        tPostVecSeq: list of successive admissible coordinates for step 1 to nDiffStep
    Once constructed, the differentiator can then be applied on different signals
    '''
    nDiffStep = 0
    paramVecSeq = [[[]]]
    tVec = [[]]
    differentiators = []
    tPostVecSeq = []
    

    def __init__(self,paramVecSeq,tVec):
        '''
        Constructor
        '''
        # Store differentiation parameters into local attributes
        self.nDiffStep = len(paramVecSeq)
        self.paramVecSeq = paramVecSeq
        self.tVec = tVec
        # Build successive differentiators
        self.buildDifferentiators()
        
    def buildDifferentiators(self):
        '''
        Construct successive differentiators
        '''
        self.differentiators.append(MultiDiff(self.paramVecSeq[0],self.tVec))
        self.tPostVecSeq.append(self.differentiators[0].tPostVec)
        for step in range(1,self.nDiffStep):
            self.differentiators.append(MultiDiff(self.paramVecSeq[step],self.tPostVecSeq[step-1]))
            self.tPostVecSeq.append(self.differentiators[step].tPostVec)
            
    
    def differentiate(self,signal):
        '''
        Numerical differentiation method
        Once the differentiator is constructed, can be applied to compute derivative estimates
        Input:
            signal: samples of the signal to differentiate
        Outputs:
            tPostSeqVec: list of estimation times per each dimension and differentation step
            dPostVec: list of derivative estimates for successive differentiation steps
        '''
        dPostSeq = []
        for step in range(self.nDiffStep):
            (_,dPost) = self.differentiators[step].differentiate(signal)
            dPostSeq.append(dPost)
        return (self.tPostVecSeq,dPostSeq)