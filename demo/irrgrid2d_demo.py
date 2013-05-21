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
from eand.irrgrid import IrrGrid2D

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

signal = []
for i in range(Ns):
    signal.append(cos(2*(t1[i]+t2[i])))

n1 = 1
alpha1 = 1
beta1 = 1
n2 = 0
alpha2 = 0
beta2 = 0
T1 = 0.25
T2 = 0.25
'''
n1 = 0
alpha1 = 0
beta1 = 0
n2 = 1
alpha2 = 1
beta2 = 1
T1 = 0.25
T2 = 0.25
'''

irrGrid2D = IrrGrid2D(n1,n2,alpha1,beta1,alpha2,beta2,t1,t2,T1,T2)

# IMPORTANT
signal = irrGrid2D.sortSignal(signal)

irrGrid2D.plotDelaunay(0)

#print irreg2D.delaunayTriangles
#print irreg2D.delaunayCircumcenters

print 'COMMENCING DIFFERENTIATION'
(t1Post,t2Post,dPost) = irrGrid2D.differentiate(signal)

tSlice,dSlice = irrGrid2D.plotSlice(t1Post,t2Post,dPost,'t1',0.,0.1)
dSliceRef = []
for i in tSlice:
    dSliceRef.append(-2*sin(2*i))
plt.plot(tSlice,dSliceRef,'r.')

irrGrid2D.plotScatter(t1Post, t2Post, dPost)

plt.show()
