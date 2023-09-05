#Parte1, clasificación de compuertas AND, OR, XOR 
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
    
    def fit(self,X,Y,epochs=50):#función de aprendizaje/entrenamiento
        p = X.shape[1]
        for _ in range(epochs):
            for i in range (p):
                y_est = self.predict(X[:,i].reshape(-1,1))
                #actualizaciones
                self.w += self.eta * (Y[i]-y_est)*X[:,i]
                self.b += self.eta * (Y[i]-y_est)*1

def draw_2d (model): #solo sirve para plotear 2d
    w1, w2, b = model.w[0],model.w[1],model.b
    li, ls = -2,2 #limites de la compuerta
    plt.plot([li,ls],
             [(1/w2)*(-w1*(li)-b),(1/w2)*(-w1*(ls)-b)], 
             '--k')

neuron = Perceptron(2, 0.1)

X = np.array([[0,0,1,1],
              [0,1,0,1]])     #X en el dataset   

#Y = np.array([0,0,0,1])#compuerta AND
#Y = np.array([1,1,1,0])#compuerta OR
Y = np.array([0,1,1,0])#compuerta XOR

#Entrenamiento de la neurona
neuron.fit(X,Y)

#Dibujo
_, p = X.shape
for i in range (p):
    if Y[i] == 0:
        plt.plot(X[0,i],X[1,i],'or')
    else:
        plt.plot(X[0,i],X[1,i],'ob')

plt.title('Perceptron | XOR')
plt.grid('on')
plt.xlim([-1,2])
plt.ylim([-1,2])
plt.xlabel(r'$x_1$')
plt.xlabel(r'$x_2$')

draw_2d(neuron)
plt.show()