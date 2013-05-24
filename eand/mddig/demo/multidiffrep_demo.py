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

import matplotlib.pyplot as plt
from math import cos,sin
import numpy as np
from eand.mddig.multidiffrep import MultiDiffRep

print 'Initializing estimation parameters...'

Ns = 500
t1Min = -1.0
t1Max = 1.0
t2Min = -1.0
t2Max = 1.0

t1 = np.array([0. for _ in range(Ns)])
t2 = np.array([0. for _ in range(Ns)])
for i in range(Ns):
    t1[i] = t1Min+(t1Max-t1Min)*np.random.random()
    t2[i] = t2Min+(t2Max-t2Min)*np.random.random()

n1 = 1
alpha1 = 3
beta1 = 3
n2 = 0
alpha2 = 0
beta2 = 0
T1 = 0.25
T2 = 0.25

# 1D case
paramVec1 = [[n1,alpha1,beta1,T1]]
paramVec2 = [[n1,alpha1,beta1,T1]]
paramVecSeq = [paramVec1,paramVec2]
tVec = [t1]
'''
# 2D case
paramVec1 = [[n1,alpha1,beta1,T1],[n2,alpha2,beta2,T2]] # differentiate first along the first axis
paramVec2 = [[n2,alpha2,beta2,T2],[n1,alpha1,beta1,T1]] # then along the second coordinate
paramVecSeq = [paramVec1,paramVec2]
tVec = [t1,t2]
'''

nDim = len(tVec)
nSamples = len(tVec[0])
nDiffStep = len(paramVecSeq)

signal = [cos(2*sum([t[i] for t in tVec])) for i in range(nSamples)]

print 'Building successive differentiators...'
multiDiffRep = MultiDiffRep(paramVecSeq,tVec)

print 'Commencing differentiation...'
(tPostVecSeq,dPostSeq) = multiDiffRep.differentiate(signal)

print 'Plotting initial signal...'
multiDiffRep.differentiators[0].plotScatter(tVec, signal,0)

print 'Plotting successive partitions...'
for step in range(nDiffStep):
    multiDiffRep.differentiators[step].plotPartition(0)
    
print 'Plotting derivative estimate...'
for step in range(len(paramVecSeq)):
    multiDiffRep.differentiators[step].plotScatter(tPostVecSeq[step], dPostSeq[step],0)
    multiDiffRep.differentiators[step].plotSurface(tPostVecSeq[step], dPostSeq[step],0)

print 'Plotting estimate slice and reference derivative...'
for step in range(nDiffStep):
    tSlice,dSlice = multiDiffRep.differentiators[step].plotSlice(tPostVecSeq[step],dPostSeq[step],1,0.,0.1,0)
    if sum([sum([paramVecSeq[i][j][0] for j in range(nDim)]) for i in range(step+1)]) == 1:
        dRef = [-2*sin(2*i) for i in tSlice]
    elif sum([sum([paramVecSeq[i][j][0] for j in range(nDim)]) for i in range(step+1)]) == 2:
        dRef = [-4*cos(2*i) for i in tSlice]
    elif sum([sum([paramVecSeq[i][j][0] for j in range(nDim)]) for i in range(step+1)]) == 3:
        dRef = [8*sin(2*i) for i in tSlice]
    plt.plot(tSlice,dRef,'r.')

plt.show()

print 'SUCCESS!'
