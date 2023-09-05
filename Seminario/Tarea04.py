#OR gate adjusting manually weights
import numpy as np
import matplotlib.pyplot as plt

w0= -1.2
w1= 0.9
w2= .5

X=np.array([[0,0,1,1],
           [0,1,0,1]])

Y=np.array([0,0,0,1])

_, p = X.shape
for i in range (p):
    if Y[i] == 0:
        plt.plot(X[0,i],X[1,i],'or')
    else:
        plt.plot(X[0,i],X[1,i],'ob')

plt.plot([-1,2],
             [(1/w2)*(-w1*(-1)-w0),(1/w2)*(-w1*(2)-w0)], 
             '--k')

plt.xlim([-1,2])
plt.ylim([-1,2])
plt.grid('on')
plt.show()