import tkinter as tk
from tkinter import filedialog


def loadFileContent():
    try:
        with open("gates.txt","r") as archivo:
            content = archivo.readlines()
        return content
    except FileNotFoundError:
        return []

def parseContent():
    content=loadFileContent()
    for i in content:
        current_gate = i.split(",")
        print(current_gate[0])
    

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

inputs_description = tk.Label(input_frame,text="X=[[0,0,1,1][1,0,1,0]]")
description = tk.Label(input_frame,text="Ingrese los pesos sinapticos:")
w0_input=tk.Entry(input_frame)
w1_input=tk.Entry(input_frame)
w2_input=tk.Entry(input_frame)
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

