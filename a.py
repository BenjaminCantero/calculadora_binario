import tkinter as tk
from tkinter import messagebox, scrolledtext

# ==== FUNCIONES BINARIAS ====

def es_binario(cadena):
    return all(d in "01" for d in cadena)

def binario_a_decimal(bin_str):
    return int(bin_str, 2)

def decimal_a_binario(num):
    return bin(num)[2:]

def suma_binaria(a, b):
    return decimal_a_binario(binario_a_decimal(a) + binario_a_decimal(b))

def resta_binaria(a, b):
    return decimal_a_binario(binario_a_decimal(a) - binario_a_decimal(b))

def multiplicacion_binaria(a, b):
    return decimal_a_binario(binario_a_decimal(a) * binario_a_decimal(b))

# ==== CALCULADORA BINARIA ====

def abrir_calculadora_binaria():
    ventana = tk.Toplevel()
    ventana.title("Calculadora Binaria")
    ventana.geometry("400x550")
    ventana.configure(bg="#f0f4f8")

    entrada = tk.Entry(ventana, font=("Consolas", 20), justify="right", bd=8)
    entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

    historial = scrolledtext.ScrolledText(ventana, width=40, height=8, font=("Consolas", 12), state="disabled", bg="#ffffff")
    historial.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    def limpiar():
        entrada.delete(0, tk.END)

    def agregar_texto(texto):
        entrada.insert(tk.END, texto)

    def agregar_historial(texto):
        historial.configure(state="normal")
        historial.insert(tk.END, texto + "\n")
        historial.configure(state="disabled")
        historial.see(tk.END)

    def operar():
        texto = entrada.get()
        try:
            if '+' in texto:
                a, b = texto.split('+')
                if not es_binario(a) or not es_binario(b): raise ValueError
                resultado = suma_binaria(a, b)
            elif '-' in texto:
                a, b = texto.split('-')
                if not es_binario(a) or not es_binario(b): raise ValueError
                resultado = resta_binaria(a, b)
            elif '*' in texto:
                a, b = texto.split('*')
                if not es_binario(a) or not es_binario(b): raise ValueError
                resultado = multiplicacion_binaria(a, b)
            else:
                raise ValueError
            agregar_historial(f"{texto} = {resultado}")
            entrada.delete(0, tk.END)
            entrada.insert(0, resultado)
        except:
            messagebox.showerror("Error", "Operación binaria inválida")

    def a_decimal():
        binario = entrada.get()
        if not es_binario(binario):
            messagebox.showerror("Error", "Número binario inválido")
            return
        resultado = binario_a_decimal(binario)
        agregar_historial(f"{binario} (bin) = {resultado} (dec)")
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))

    botones = [
        ('1', 1, 0), ('0', 1, 1), ('+', 1, 2), ('-', 1, 3),
        ('*', 2, 0), ('C', 2, 1), ('=', 2, 2), ('a Dec', 2, 3)
    ]

    for (texto, fila, col) in botones:
        if texto == '=':
            cmd = operar
            color = "#4CAF50"
        elif texto == 'C':
            cmd = limpiar
            color = "#f44336"
        elif texto == 'a Dec':
            cmd = a_decimal
            color = "#2196F3"
        else:
            cmd = lambda t=texto: agregar_texto(t)
            color = "#e0e0e0"

        tk.Button(ventana, text=texto, font=("Arial", 14), bg=color, activebackground="#d0d0d0",
                  command=cmd, height=2)\
            .grid(row=fila, column=col, sticky="nsew", padx=5, pady=5)

    for i in range(5):
        ventana.grid_rowconfigure(i, weight=1)
    for j in range(4):
        ventana.grid_columnconfigure(j, weight=1)

# ==== CALCULADORA DECIMAL ====

def abrir_calculadora_decimal():
    ventana = tk.Toplevel()
    ventana.title("Calculadora Decimal")
    ventana.geometry("400x600")
    ventana.configure(bg="#f9f9f9")

    entrada = tk.Entry(ventana, font=("Consolas", 20), justify="right", bd=8)
    entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

    historial = scrolledtext.ScrolledText(ventana, width=40, height=10, font=("Consolas", 12), state="disabled", bg="#ffffff")
    historial.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

    def limpiar():
        entrada.delete(0, tk.END)

    def agregar_texto(texto):
        entrada.insert(tk.END, texto)

    def agregar_historial(texto):
        historial.configure(state="normal")
        historial.insert(tk.END, texto + "\n")
        historial.configure(state="disabled")
        historial.see(tk.END)

    def calcular():
        try:
            expr = entrada.get()
            resultado = eval(expr)
            agregar_historial(f"{expr} = {resultado}")
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
        except:
            messagebox.showerror("Error", "Expresión no válida")

    def convertir_a_binario():
        try:
            numero = int(entrada.get())
            if numero < 0:
                raise ValueError
            binario = decimal_a_binario(numero)
            agregar_historial(f"{numero} (dec) = {binario} (bin)")
            entrada.delete(0, tk.END)
            entrada.insert(0, binario)
        except:
            messagebox.showerror("Error", "Ingrese un número decimal válido")

    botones = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('a Bin', 5, 0, 4)
    ]

    for boton in botones:
        texto = boton[0]
        fila = boton[1]
        col = boton[2]
        colspan = boton[3] if len(boton) == 4 else 1

        if texto == '=':
            cmd = calcular
            color = "#4CAF50"
        elif texto == 'C':
            cmd = limpiar
            color = "#f44336"
        elif texto == 'a Bin':
            cmd = convertir_a_binario
            color = "#2196F3"
        else:
            cmd = lambda t=texto: agregar_texto(t)
            color = "#e0e0e0"

        tk.Button(ventana, text=texto, font=("Arial", 14), bg=color, activebackground="#d0d0d0",
                  command=cmd, height=2)\
            .grid(row=fila, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)
    for j in range(4):
        ventana.grid_columnconfigure(j, weight=1)

# ==== MENÚ PRINCIPAL ====

root = tk.Tk()
root.title("Calculadora Principal")
root.geometry("320x240")
root.configure(bg="#ffffff")
root.resizable(False, False)

tk.Label(root, text="Elige tipo de calculadora", font=("Arial", 14), bg="#ffffff").pack(pady=20)

tk.Button(root, text="Calculadora Binaria", font=("Arial", 12), width=25,
          bg="#bbdefb", activebackground="#90caf9", command=abrir_calculadora_binaria).pack(pady=5)

tk.Button(root, text="Calculadora Decimal", font=("Arial", 12), width=25,
          bg="#c8e6c9", activebackground="#a5d6a7", command=abrir_calculadora_decimal).pack(pady=5)

tk.Button(root, text="Salir", font=("Arial", 12), width=25,
          bg="#ffcdd2", activebackground="#ef9a9a", command=root.destroy).pack(pady=10)

root.mainloop()
