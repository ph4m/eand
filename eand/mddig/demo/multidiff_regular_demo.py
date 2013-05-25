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
from eand.mddig.multidiff import MultiDiff

print 'Initializing estimation parameters...'

Ns = 500
t1Min = -1.0
t1Max = 1.0
t2Min = -1.0
t2Max = 1.0

nSamplesSorted = [25,25]
dtVec = [(t1Max-t1Min)/nSamplesSorted[0],(t2Max-t2Min)/nSamplesSorted[1]]
tProto = np.arange(-1.,1.05,0.05)
t1 = []
t2 = []
for i in tProto:
    for j in tProto:
        t1.append(i)
        t2.append(j)

n1 = 1
alpha1 = 3
beta1 = 3
n2 = 0
alpha2 = 0
beta2 = 0
T1 = 0.25
T2 = 0.25

'''
# 1D case
paramVec = [[n1,alpha1,beta1,T1]]
tVec = [t1]
'''
# 2D case
paramVec = [[n1,alpha1,beta1,T1],[n2,alpha2,beta2,T2]]
tVec = [t1,t2]

nDim = len(tVec)
nSamples = len(tVec[0])

signal = [cos(2*sum([t[i] for t in tVec])) for i in range(nSamples)]

tVec = np.array(tVec)
alreadySorted = 2
nSamplesSorted = [len(tProto),len(tProto)]

toNextValueSorted = [round(np.product([nSamplesSorted[dim] for dim in range(i+1,alreadySorted)])) for i in range(alreadySorted)]

dtVec = [tVec[i][toNextValueSorted[i]]-tVec[i][0] for i in range(alreadySorted)]

print 'Building differentiator...'
multiDiff = MultiDiff(paramVec,tVec,alreadySorted,nSamplesSorted)

print 'Plotting partition...'
multiDiff.plotPartition(0)

print 'Commencing differentiation...'
(tPostVec,dPost) = multiDiff.differentiate(signal)

print 'Calculating reference derivative...'
tSlice,dSlice = multiDiff.plotSlice(tPostVec,dPost,1,0.,0.1,0)
if sum([paramVec[i][0] for i in range(nDim)]) == 1:
    dRef = [-2*sin(2*i) for i in tSlice]
elif sum([paramVec[i][0] for i in range(nDim)]) == 2:
    dRef = [-4*cos(2*i) for i in tSlice]
plt.plot(tSlice,dRef,'r.')

print 'Plotting derivative estimate...'
multiDiff.plotScatter(tPostVec, dPost,0)
multiDiff.plotSurface(tPostVec, dPost,0)

plt.show()

print 'SUCCESS!'
'''
'''

