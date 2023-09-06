import tkinter as tk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import numpy as np

def loadFileContent():
    try:
        with open("gates.txt","r") as archivo:
            content = archivo.readlines()
        return content
    except FileNotFoundError:
        return []

def parseContent():
    X=np.array([[0,0,1,1],
           [0,1,0,1]])
    content=loadFileContent()
    for i in content:
        i = i.strip('\n')
        current_gate = i.split(",")
        if activeGate() == current_gate[0]:
            Y=np.array([current_gate[1:]])
        
    w0=w0i.get()
    w1=w1i.get()
    w2=w2i.get()
    mostrar_grafica(window,X, Y,float(w0),float(w1),float(w2))
    OR_gate.config(state="normal")
    AND_gate.config(state="normal")
    XOR_gate.config(state="normal")
def mostrar_grafica(ventana,X, Y,w0,w1,w2):
    # Crear una figura de Matplotlib
    figura = Figure(figsize=(6, 4))
    grafica = figura.add_subplot(111)
    _, p = X.shape
    for i in range (p):
        if Y[0][i] == '0':
            grafica.plot(X[0,i],X[1,i],'or')
        elif Y[0][i] == '1':
            grafica.plot(X[0,i],X[1,i],'xb')
    grafica.plot([-1,2],
             [(1/w2)*(-w1*(-1)-w0),(1/w2)*(-w1*(2)-w0)], 
             '--k')

    # grafica.xlim([-1,2])
    # grafica.ylim([-1,2])
    grafica.grid('on')
    # grafica.show()

    # Si ya hay un lienzo, lo destruye antes de crear uno nuevo
    if hasattr(mostrar_grafica, 'canvas'):
        mostrar_grafica.canvas.get_tk_widget().destroy()

    # Crear un lienzo de Matplotlib en la ventana de Tkinter
    mostrar_grafica.canvas = FigureCanvasTkAgg(figura, master=ventana)
    mostrar_grafica.canvas.get_tk_widget().pack()


        
    
def activeGate():
    if OR_gate.cget("state") == "normal":
        return "OR"
    elif AND_gate.cget("state") == "normal":
        return "AND"
    else:
        return "XOR"

    



def orSelected():
    AND_gate.config(state="disabled")
    XOR_gate.config(state="disabled")
def andSelected():
    OR_gate.config(state="disabled")
    XOR_gate.config(state="disabled")
def xorSelected():
    OR_gate.config(state="disabled")
    AND_gate.config(state="disabled")

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
#RIGHT COLUMN ELEMENTS--------------------------
input_frame = tk.Frame(window)
input_frame.pack(side="right", padx=5, pady=5)
w0i = tk.StringVar()
w1i = tk.StringVar()
w2i = tk.StringVar()

inputs_description = tk.Label(input_frame,text="X=[[0,0,1,1][1,0,1,0]]")
description = tk.Label(input_frame,text="Ingrese los pesos sinapticos:")
w0_input=tk.Entry(input_frame, textvariable=w0i)
w1_input=tk.Entry(input_frame, textvariable=w1i)
w2_input=tk.Entry(input_frame, textvariable=w2i)
OK_btn = tk.Button(input_frame, text="Aceptar", width=10,height=1, command=parseContent)

inputs_description.pack(pady=5)
description.pack(pady=5)
w0_input.pack(pady=5)
w1_input.pack(pady=5)
w2_input.pack(pady=5)
OK_btn.pack(pady=5)
#----------------------------------------------------   


window.geometry("600x500")
window.resizable(False, False)
window.mainloop()

