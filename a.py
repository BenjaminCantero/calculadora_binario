import tkinter as tk
from tkinter import messagebox

# Función para evaluar la expresión ingresada
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", "Expresión no válida")

# Función para agregar texto a la entrada
def agregar_texto(texto):
    entrada.insert(tk.END, texto)

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.resizable(False, False)

# Entrada para mostrar la expresión
entrada = tk.Entry(ventana, font=("Arial", 18), justify="right", bd=10)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Creación de los botones
for (texto, fila, columna) in botones:
    if texto == "=":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=calcular)
    elif texto == "C":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=limpiar)
    else:
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), 
                           command=lambda t=texto: agregar_texto(t))
    boton.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

# Configuración del tamaño de las filas y columnas
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for j in range(4):
    ventana.grid_columnconfigure(j, weight=1)

# Ejecutar la aplicación
ventana.mainloop()