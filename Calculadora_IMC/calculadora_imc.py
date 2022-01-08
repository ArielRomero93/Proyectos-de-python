#Calculadora de IMC

import tkinter as tk

class IMC:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de IMC")
        self.ventana.geometry("600x400")
        self.ventana.resizable(0,0)


        #ingresar datos

        self.banda = tk.Label(self.ventana, bg="blue", text="  IMC  ", font=("Arial", 20))
        self.banda.grid(row=0)

        self.Estatura = tk.Label(self.ventana, text="Estatura en centimetros:", font=("Arial", 10))
        self.Estatura.grid(row=1, column=0)

        self.Dato_estatura = tk.StringVar()
        self.Caja1 = tk.Entry(self.ventana, width=10, textvariable=self.Dato_estatura)
        self.Caja1.grid(row=1, column=1)

        self.Peso = tk.Label(self.ventana, text="Peso en kilogramos:", font=("Arial", 10))
        self.Peso.grid(row=2, column=0)
        
        self.Dato_peso = tk.StringVar()
        self.Caja2 = tk.Entry(self.ventana, width=10, textvariable=self.Dato_peso)
        self.Caja2.grid(row=2, column=1)

        self.Boton_calculo = tk.Button(self.ventana, text="Calcular", font=("Arial", 10), width=20, height=2, command=self.calcularIMC)
        self.Boton_calculo.grid(row=3, column=0, columnspan=2)

        self.Resultado = tk.Label(self.ventana, text="Resultado:", font=("Arial", 10))
        self.Resultado.grid(row=1, column=3)

        self.Mostrar_resultado = tk.Label(self.ventana, text="", font=("Arial", 10))
        self.Mostrar_resultado.grid(row=2, column=4)
        self.ventana.mainloop()

    
    def calcularIMC(self):
        self.estatura = float(self.Dato_estatura.get())
        self.peso = float(self.Dato_peso.get())
        #imc
        self.IMC = self.peso / (self.estatura/100)**2

        #peso mínimo
        self.P_min = ((self.estatura/100)**2)*18.6
        #peso ideal
        self.P_Ideal = ((self.estatura/100)**2)*21
        #peso máximo
        self.P_Max = ((self.estatura/100)**2)*25

        if self.IMC < 16:
            self.banda = "Delgadez severa"
        elif self.IMC >= 16 and self.IMC < 17:
            self.banda = "Delgadez moderada"
        elif self.IMC >= 17 and self.IMC < 18.5:
            self.banda = "Delgadez aceptable"
        elif self.IMC >= 18.5 and self.IMC < 25:
            self.banda = "Peso normal"
        elif self.IMC >= 25 and self.IMC < 30:
            self.banda = "Sobrepeso"
        elif self.IMC >= 30 and self.IMC < 35:
            self.banda = "Obesidad grado I"
        elif self.IMC >= 35 and self.IMC < 40:
            self.banda = "Obesidad grado II"
        elif self.IMC >= 40:
            self.banda = "Obesidad grado III"

        self.Mostrar_resultado.config(text=f'Su indice de masa corporal es {round(self.IMC, 2)}\nUsted tiene {self.banda}\n\nPeso mínimo saludable es de: {round(self.P_min)}\nPeso ideal es de: {round(self.P_Ideal)}\nPeso máximo saludable: {round(self.P_Max)}')


ventana = IMC()


















