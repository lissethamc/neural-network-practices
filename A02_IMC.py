#Clasificación de IMC de diferentes personas, si tienen sobrepeso o no
import matplotlib.pyplot as plt
import numpy as np

D=5
X = np.zeros([2,D])
Y = np.zeros([D])

X_norm = np.zeros([2,D])
Y_norm = np.zeros([D])


#x1 = altura cm
#x2 = peso
#x3 = IMC
p=X.shape[1]
for i in range(p):
    X[0][i]=np.random.randint(150,180+1) #altura
    X[1][i]=np.random.randint(44,120+1) #peso
    
    Y[i] = (X[1][i])/(float(X[0][i]/100)**2)


X_sort = np.sort(X)
Y_sort = np.sort(Y)

p=X.shape[1]
for i in range(p):
    X_norm[0][i] = (X[0][i]- X_sort[0][0])/ (X_sort[0][D-1] -  X_sort[0][0])
    X_norm[1][i] = (X[1][i]- X_sort[1][0])/ (X_sort[1][D-1] -  X_sort[1][0])

    Y_norm[i] = (Y[i]- Y_sort[0])/ (Y_sort[D-1] -  Y_sort[0])




#Dibujo
_, p = X.shape
for i in range (p):
    if Y[i] > 25:
        plt.plot(X_norm[0,i],X_norm[1,i],'or')
    else:
        plt.plot(X_norm[0,i],X_norm[1,i],'ob')
plt.show()