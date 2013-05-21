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
from eand.irrgrid import IrrGrid1D

Ns = 1000
t1Min = -1.0
t1Max = 1.0

t1 = np.array([0. for _ in range(Ns)])
for i in range(Ns):
    t1[i] = t1Min+(t1Max-t1Min)*np.random.random()

signal = []
for i in range(Ns):
    signal.append(cos(2*(t1[i])))

n1 = 1
alpha1 = 1
beta1 = 1
T1 = 0.25
'''
n1 = 0
alpha1 = 0
beta1 = 0
T1 = 0.25
'''

irrGrid1D = IrrGrid1D(n1,alpha1,beta1,t1,T1)

# IMPORTANT
signal = irrGrid1D.sortSignal(signal)

irrGrid1D.plotPartition(0)

#print irreg1D.partitionSegments
#print irreg1D.partitionCenters

print 'COMMENCING DIFFERENTIATION'
(t1Post,dPost) = irrGrid1D.differentiate(signal)

'''
tSlice,dSlice = irreg2D.plotSlice(t1Post,t2Post,dPost,'t1',0.,0.1)
dSliceRef = []
for i in tSlice:
    dSliceRef.append(-2*sin(2*i))
plt.plot(tSlice,dSliceRef,'r.')
'''

irrGrid1D.plotScatter(t1Post, dPost)
dSliceRef = []
for i in t1Post:
    dSliceRef.append(-2*sin(2*i))
plt.plot(t1Post,dSliceRef,'r.')

plt.show()
