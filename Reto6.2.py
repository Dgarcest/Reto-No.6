"""
Dado la figura de la imagen, desarrolle:
Una función matemática para calcular el área y el perimetro.
Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
Revise como utilizar el valor de pi usando import math y math.pi
"""

import math

def Area(r, a, b):
    Area_total = a*b + (math.pi*r**2)*2
    return Area_total

def Perimetro(r, a, b):
    Perimetro_total = (2*math.pi*r)*2 + a*2 + b*2
    return Perimetro_total

if __name__ == "__main__":
    r = float(input("Ingrese el valor de el radio: "))
    a = float(input("Ingrese el ancho del cuadrado: "))
    b = float(input("Ingrese el largo del cuadrado: "))
    Area_t = Area(r, a, b)
    Perimetro_t = Perimetro(r, a, b)

    print(f"El area total es de {Area_t} y el perimetro total es de {Perimetro_t}")