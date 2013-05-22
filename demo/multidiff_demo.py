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

Ns = 1000
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
alpha1 = 1
beta1 = 1
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

signal = [cos(2*sum([t[i] for t in tVec])) for i in range(len(tVec[0]))]

print 'Buiding differentiator...'
multiDiff = MultiDiff(paramVec,tVec)

print 'Plotting partition...'
multiDiff.plotPartition(0)

print 'Commencing differentiation...'
(tPostVec,dPost) = multiDiff.differentiate(signal)

print 'Calculating reference derivative...'
tSlice,dSlice = multiDiff.plotSlice(tPostVec,dPost,1,0.,0.1)
dRef = []
for i in tSlice:
    dRef.append(-2*sin(2*i))
plt.plot(tSlice,dRef,'r.')

print 'Plotting derivative estimate...'
multiDiff.plotScatter(tPostVec, dPost)
multiDiff.plotSurface(tPostVec, dPost)

plt.show()

print 'SUCCESS!'


