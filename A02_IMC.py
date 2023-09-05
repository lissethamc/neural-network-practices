#Clasificación de IMC de diferentes personas, si tienen sobrepeso o no
import matplotlib.pyplot as plt
import numpy as np

class Perceptron:
    def __init__(self, n_input, learning_rate): #el numero de entradas define la arquitectura de la neurona
        self.w = -1 + 2*np.random.rand(n_input) #vector aleatorio (para no sesgar los conocimientos)d e pesos sinapticos entre -1 y 1
        self.b = -1 + 2*np.random.rand()
        self.eta = learning_rate

    def predict(self,X):
        p = X.shape[1] #tamaño de la xmatriz x, 0 indexado, por lo que retorna las columnas
        y_est = np.zeros(p) #vector de y estimadas 
        for i in range(p):
            y_est[i]=np.dot(self.w,X[:,i])+self.b #para y_est[i], es el producto punto entre el vector X en la columna i y el vector w, más el bias
            if y_est[i] >= 0:
                y_est[i] = 1
            else:
                y_est[i] = 0
        return y_est
    
    def fit(self,X,Y,epochs=400):#función de aprendizaje/entrenamiento
        p = X.shape[1]
        for _ in range(epochs):
            for i in range (p):
                y_est = self.predict(X[:,i].reshape(-1,1))
                #actualizaciones
                self.w += self.eta * (Y[i]-y_est)*X[:,i]
                self.b += self.eta * (Y[i]-y_est)*1

def draw_2d (model): #solo sirve para plotear 2d
    w1, w2, b = model.w[0],model.w[1],model.b
    li, ls = 0,1 #limites de la compuerta
    plt.plot([li,ls],
             [(1/w2)*(-w1*(li)-b),(1/w2)*(-w1*(ls)-b)], 
             '--k')

neuron = Perceptron(2, 0.5)  

D=15
X = np.zeros([2,D])
Y = np.zeros([D])

X_norm = np.zeros([2,D])
Y_norm = np.zeros([D])


#x1 = altura cm
#x2 = peso
#x3 = IMC
p=X.shape[1]
for i in range(p):
    X[0][i]=np.random.randint(150,180+1) #altura cm
    X[1][i]=np.random.randint(44,120+1) #peso
    
    Y[i] = (X[1][i])/(float(X[0][i]/100)**2)


X_sort = np.sort(X)
Y_sort = np.sort(Y)

#normalizacion
p=X.shape[1]
for i in range(p):
    X_norm[0][i] = (X[0][i]- X_sort[0][0])/ (X_sort[0][D-1] -  X_sort[0][0])
    X_norm[1][i] = (X[1][i]- X_sort[1][0])/ (X_sort[1][D-1] -  X_sort[1][0])

    Y_norm[i] = (Y[i]- Y_sort[0])/ (Y_sort[D-1] -  Y_sort[0])

#Dibujo
_, p = X.shape
for i in range (p):
    if Y[i] > 25:
        Y_norm[i]=1
        plt.plot(X_norm[0,i],X_norm[1,i],'or')
    else:
        Y_norm[i]=0
        plt.plot(X_norm[0,i],X_norm[1,i],'ob')
neuron.fit(X_norm,Y_norm)

plt.title('Cálculo de IMC | Perceptrón')
plt.grid('on')
plt.xlim([-0.05,1.05])
plt.ylim([-0.05,1.05])
plt.xlabel(r'$Altura$')
plt.ylabel(r'$Peso$')

draw_2d(neuron)
plt.show()