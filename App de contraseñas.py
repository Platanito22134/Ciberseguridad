import tkinter as tk
import tkinter as tkk
import random
import string

def generar_numero():
    numeros_aleatorios = string.digits
    contrasena = ""
    for _ in range(10):
        caracter = random.choice(numeros_aleatorios)
        contrasena += caracter
    label_contrasena.config(text=contrasena)

def generar_contrasenacorta():
    letras_mayusculas = string.ascii_uppercase
    contrasena = ""
    for _ in range(4):
        caracter = random.choice(letras_mayusculas)
        contrasena += caracter
    label_contrasena.config(text=contrasena)

def generar_contrasenapersonalizada():
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros_aleatorios = string.digits
    digitos = string.digits
    especiales = "!@#$%^&*()"

    contrasena = ""
    contrasena += random.choice(letras_mayusculas)
    contrasena += random.choice(especiales)

    for _ in range(12):
        caracter = random.choice(letras_mayusculas + letras_minusculas + digitos + especiales)
        contrasena += caracter

        random.shuffle(list(contrasena))
    contrasena = ''.join(contrasena)
    
    label_contrasena.config(text=contrasena)


ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.configure(bg="#303030")

boton_corta = tk.Button(ventana, text="Generar Contraseña Corta", command=generar_contrasenacorta)
boton_corta.pack()

boton_personalizada = tk.Button(ventana, text="Generar Contraseña Personalizada", command=generar_contrasenapersonalizada)
boton_personalizada.pack()

boton_personalizada = tk.Button(ventana, text="Generar Contraseña Numerica", command=generar_numero)
boton_personalizada.pack()

label_contrasena = tk.Label(ventana, text="Tu contraseña aparecerá aquí")
label_contrasena.pack()

ventana.mainloop()
