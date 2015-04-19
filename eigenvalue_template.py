import numpy as np
import math
import matplotlib.pyplot as plt
from TJMatrix import agreement_matrix


"""A is our adjacency matrix with people along both axes and their
voting percentages in the matrix"""

#A = np.matrix('4 2 1; 1 4 5; 3 3 2')
A = agreement_matrix
# 
ATA = A.transpose() * A
evecs_ATA = np.linalg.eig(ATA)[1]
evals_ATA = np.linalg.eig(ATA)[0]
V = evecs_ATA

AAT = A * A.transpose()
evecs_AAT = np.linalg.eig(AAT)[1]
evals_AAT = np.linalg.eig(AAT)[0]
U = evecs_AAT

sigmas = []
for eigenvalue in evals_AAT:
	square_root = math.sqrt(eigenvalue)
	sigmas.append(square_root)

S = np.diag(sigmas)

sig1u1v1t = math.sqrt(evals_AAT[1]) * U[:,1] * V.transpose() [1,:]
sig2u2v2t = A - sig1u1v1t

x1 = sig1u1v1t[0,:]
x2 = sig2u2v2t[0,:]
y1 = sig1u1v1t[1,:]
y2 = sig2u2v2t[1,:]

plt.subplot(2,1,1)
plt.plot(x1,y1, 'ko')
plt.title('First singular decomposition')

plt.subplot(2,1,2)
plt.plot(x2,y2, 'ro')
plt.title('Second singular decomposition')

plt.show()