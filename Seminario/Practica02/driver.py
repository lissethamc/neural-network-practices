import numpy as np

def loadFileContent():
    try:
        with open("Seminario\Practica02\gates.txt","r") as archivo:
            content = archivo.readlines()
        return content
    except FileNotFoundError:
        print("adios")
        return []

def parseContent(a,b,c):
    content=loadFileContent()
    for i in content:
        i = i.strip('\n')
        current_gate = i.split(",")
        if activeGate(a,b,c) == current_gate[0]:    
            arry=np.array(current_gate[1:])
            Y = arry.astype(int)
            return Y
  
def activeGate(a,b,c):
    if a.cget("state") == "normal":
        return "OR"
    elif b.cget("state") == "normal":
        return "AND"
    else:
        return "XOR"
