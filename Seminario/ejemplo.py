import tkinter as tk
from tkinter import ttk

def obtener_texto():
    texto_ingresado = entrada.get()
    etiqueta_resultado.config(text=f"Texto ingresado: {texto_ingresado}")

ventana = tk.Tk()
ventana.title("Entradas de Texto con Placeholders")

# Crear un objeto de estilo para Entry con marcador de posición
style = ttk.Style()
style.configure("Placeholder.TEntry", foreground="gray")

# Barra para ingresar texto (Entry) con marcador de posición
entrada = ttk.Entry(ventana, style="Placeholder.TEntry")
entrada.insert(0, "Escribe aquí...")  # Texto de marcador de posición
entrada.pack(pady=5)

# Botón para obtener el texto ingresado
boton_obtener_texto = ttk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton_obtener_texto.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
