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

import Image
import numpy as np
from matplotlib import pyplot as plt
from eand.kmand import MonoDiff

'''
Image processing example: numerical differentiation for edge detection
Original image: http://www.flickr.com/photos/ph4m/ (CC-BY-NC-SA)
'''

# Loading picture
picture = Image.open('sciencecat.jpg')
data = list(picture.getdata())

# Differentiator initialization
n = 1
N = 1
kappa = 0
mu = 0
M = 5
Ts = 1.
xi = 0.5
lambdaOptType = 'noisyenv'
causality = 'causal'
flagCompleteTime = 'none'
monoDiff = MonoDiff(n,N,kappa,mu,M,Ts,xi,lambdaOptType,causality,flagCompleteTime)

# Taking RGB mean
nCol,nRow = picture.size
tRow = range(nRow)
tCol = range(nCol)
print 'Picture size:', nCol,nRow
imgReshape = np.array(data).reshape(nRow,nCol,3)
imgMean = [[np.mean(imgReshape[row][col]) for col in tCol] for row in tRow]

# Differentiating through columns
imgDiffByCol = []
for row in tRow:
    signal = imgMean[row]
    (tColPost,dPost) = monoDiff.differentiate(tCol,signal)
    imgDiffByCol.append(abs(dPost))
imgDiffByCol = np.array(imgDiffByCol)/np.max(imgDiffByCol)

# Differentiating through rows
imgDiffByRow = []
for col in tCol:
    signal = [imgMean[row][col] for row in tRow]
    (tRowPost,dPost) = monoDiff.differentiate(tRow,signal)
    imgDiffByRow.append(abs(dPost))
imgDiffByRow = (np.array(imgDiffByRow)/np.max(imgDiffByRow)).transpose()

# Resetting w.r.t. delay
imgDiffByCol = imgDiffByCol[tRowPost]
imgDiffByRow = [imgDiffByRow[row][tColPost] for row in range(len(imgDiffByRow))]

# Taking the average
imgEdges = [[[0.5*(imgDiffByCol[row][col] + imgDiffByRow[row][col]) for _ in range(3)] for col in range(len(tColPost))] for row in range(len(tRowPost))]
plt.figure()
plt.imshow(imgEdges)

# Threshold
imgEdgesThreshold = [[[(imgEdges[row][col][chan] > 0.1)*imgEdges[row][col][chan] for chan in range(3)] for col in range(len(tColPost))] for row in range(len(tRowPost))]
plt.figure()
plt.imshow(imgEdgesThreshold)

plt.show()
