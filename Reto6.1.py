"""
Dado la figura de la imagen, desarrolle:
-Una función matemática para calcular el volumen y el área superficial.
-Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
-Revise como utilizar el valor de pi usando import math y math.pi
"""

import math

def Volumen(r1, r2, h):
    global Volumen_esfera
    global Volumen_cono
    Volumen_esfera = (4*math.pi*(r1**3))/3
    Volumen_cono = (math.pi*(r2**2)*h)/3
    Volumen_total = Volumen_esfera + Volumen_cono
    return Volumen_total


def Superficie(r1, r2, h):
    global Superficie_esfera
    global Superficie_cono
    Superficie_esfera = 4*math.pi*r1**2
    g = (h**2 + r2**2)**(1/2)
    Superficie_cono = math.pi*g*r2 + math.pi*r2**2
    Superficie_total = Superficie_esfera + Superficie_cono
    return Superficie_total


if __name__ == "__main__":
    r1 = float(input("Ingrese el valor de el radio de la esfera: "))
    r2 = float(input("Ingrese el valor de el radio de el cono: "))
    h = float(input("Ingrese el valor de la altura del cono: "))
    Volumen_t = Volumen(r1, r2, h)
    Superficie_t = Superficie(r1, r2, h)

    print(f"El valor del volumen total es de {Volumen_t} y el valor de la superficie total es de {Superficie_t}")
    print(f"El volumen de la esfera es de {Volumen_esfera} y el del cono el de {Volumen_cono}")
    print(f"La superficie de la esfera es de {Superficie_esfera} y la del cono el de {Superficie_cono}")