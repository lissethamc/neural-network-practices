from perceptron import Perceptron
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
import tkinter as tk
from driver import *

def main():
    def getModelData(neuron,X,Y):
        yest = neuron.predict(X)
        mean_accuracy_lbl.config(text=f"{accuracy_score(Y,yest)}")
        confusion_matrix_lbl.config(text=f"{confusion_matrix(Y, yest)}")
        f1_score_lbl.config(text=f"{f1_score(Y, yest)}")

        #WINDOW -DRIVERS-------------------------------------------------------------------------------
  
    def orSelected():
        AND_gate.config(state="disabled")
        XOR_gate.config(state="disabled")
        X=np.array([[0,0,1,1],
                [0,1,0,1]])
      
        Y=parseContent(OR_gate,AND_gate,XOR_gate)
        neurona = Perceptron(2, 0.1)
        neurona.fit(X,Y)
        mostrar_grafica(window,X,Y,neurona.b,neurona.w[0],neurona.w[1])
        OR_gate.config(state="normal")
        AND_gate.config(state="normal")
        XOR_gate.config(state="normal")
        getModelData(neurona,X,Y)
        return neurona,X,Y

    def andSelected():
        OR_gate.config(state="disabled")
        XOR_gate.config(state="disabled")
        X=np.array([[0,0,1,1],
                [0,1,0,1]])
        Y=parseContent(OR_gate,AND_gate,XOR_gate)
        neurona = Perceptron(2, 0.1)
        neurona.fit(X,Y)
        mostrar_grafica(window,X,Y,neurona.b,neurona.w[0],neurona.w[1])
        OR_gate.config(state="normal")
        AND_gate.config(state="normal")
        XOR_gate.config(state="normal")
        getModelData(neurona,X,Y)
        return neurona,X,Y
        
    def xorSelected():
        OR_gate.config(state="disabled")
        AND_gate.config(state="disabled")
        X=np.array([[0,0,1,1],
                [0,1,0,1]])
        Y=parseContent(OR_gate,AND_gate,XOR_gate)
        neurona = Perceptron(2, 0.1)
        neurona.fit(X,Y)
        mostrar_grafica(window,X,Y,neurona.b,neurona.w[0],neurona.w[1])
        OR_gate.config(state="normal")
        AND_gate.config(state="normal")
        XOR_gate.config(state="normal")
        getModelData(neurona,X,Y)
        return neurona,X,Y


    #WINDOW ----------------------------------------------------------------------------

    window = tk.Tk()
    window.title("Perceptrón")
    #TOP ELEMENTS -----------------------------
    button_frame = tk.Frame(window)
    button_frame.pack(side="top", padx=5, pady=5)

    OR_gate = tk.Button(button_frame, text="OR", width=10,height=1, command = orSelected)
    AND_gate = tk.Button(button_frame, text="AND",width=10,height=1, command = andSelected)
    XOR_gate = tk.Button(button_frame, text="XOR",width=10,height=1, command = xorSelected)
    
    OR_gate.pack(side="left", padx=5)
    AND_gate.pack(side="left", padx=5)
    XOR_gate.pack(side="left", padx=5)

    window.geometry("600x500")
    window.resizable(False, False)

    #RIGHT COLUMN ELEMENTS--------------------------
    modelDataFrame = tk.Frame(window)
    modelDataFrame.pack(side="right", padx=40, fill="y", expand=True)

    mean_title_lbl = tk.Label(modelDataFrame,text="Mean Accuracy", pady=30)
    mean_title_lbl.pack(anchor="n")
    mean_accuracy_lbl = tk.Label(modelDataFrame)
    mean_accuracy_lbl.pack(anchor="n")

    confusion_title_lbl = tk.Label(modelDataFrame,text="Confusion Matrix", pady=30)
    confusion_title_lbl.pack(anchor="n")
    confusion_matrix_lbl = tk.Label(modelDataFrame)
    confusion_matrix_lbl.pack(anchor="n")

    confusion_title_lbl = tk.Label(modelDataFrame,text="F1 Score",pady=30)
    confusion_title_lbl.pack(anchor="n")
    f1_score_lbl = tk.Label(modelDataFrame)
    f1_score_lbl.pack(anchor="n")



    #WINDOW SHOW---------------------------------------------------------------------------------------------
    def mostrar_grafica(ventana,X, Y,w0,w1,w2):
        figura = Figure(figsize=(6, 4))
        grafica = figura.add_subplot(111)
        _, p = X.shape
        for i in range (p):
            if Y[i] == 0:
                grafica.plot(X[0,i],X[1,i],'or')
            elif Y[i] == 1:
                grafica.plot(X[0,i],X[1,i],'xb')
        grafica.plot([-1,2],
                [(1/w2)*(-w1*(-1)-w0),(1/w2)*(-w1*(2)-w0)], 
                '--k')

        grafica.grid('on')
        if hasattr(mostrar_grafica, 'canvas'):
            mostrar_grafica.canvas.get_tk_widget().destroy()

        mostrar_grafica.canvas = FigureCanvasTkAgg(figura, master=ventana)
        mostrar_grafica.canvas.get_tk_widget().pack(side="left", padx=10)

    #PERCEPTRON-----------------------------------------------------------------------------------
    
    currentGate = activeGate (OR_gate,AND_gate,XOR_gate)
    if currentGate == "OR":
        currentNeuron,X,Y = orSelected()
    elif currentGate == "AND":
        currentNeuron,X,Y = andSelected()
    else :
        currentNeuron,X,Y = xorSelected()

    
    window.mainloop()
    
if __name__ == "__main__":
    main()


