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

neuron = Perceptron(2, 0.1)

X = np.array([[0,0,1,1],
              [0,1,0,1]])     #X en el dataset   

Y = np.array([0,0,0,1])#compuerta AND 