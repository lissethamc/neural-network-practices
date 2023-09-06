import tkinter as tk

def habilitar_boton():
    boton.config(state="normal")  # Habilitar el botón

def deshabilitar_boton():
    boton.config(state="disabled")  # Deshabilitar el botón

ventana = tk.Tk()
ventana.title("Botón Habilitado/Desabilitado")

# Crear un botón
boton = tk.Button(ventana, text="Botón", state="normal")  # Estado normal (habilitado) por defecto
boton.pack()

# Botones para habilitar y deshabilitar
boton_habilitar = tk.Button(ventana, text="Habilitar", command=habilitar_boton)
boton_deshabilitar = tk.Button(ventana, text="Deshabilitar", command=deshabilitar_boton)

boton_habilitar.pack()
boton_deshabilitar.pack()

ventana.mainloop()
