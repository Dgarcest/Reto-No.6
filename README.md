# Reto-No.6

1. Dado la imagen desarrolle:
   
<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="800" height="auto"/></br>
</div>
     
*Una función matemática para calcular el volumen y el área superficial.
   
*Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h
   
*Revise como utilizar el valor de pi usando *import math* y *math.pi*

```python
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
    print(f"El volumen de la esfera es de {Volumen_esfera} y el del cono es de {Volumen_cono}")
    print(f"La superficie de la esfera es de {Superficie_esfera} y la del cono es de {Superficie_cono}")
```

2. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="800" height="auto"/></br>
</div>

* Una función matemática para calcular el área y el perimetro.
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
* Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python
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
```

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
def Cantidad(N, M, K):
    Gallinas = N*6
    Gallos = M*7
    Pollitos = K*1
    global Carne
    Carne = Gallinas + Gallos + Pollitos

if __name__ == "__main__":
    N = int(input("Ingrese la cantidad de gallinas: "))
    M = int(input("Ingrese la cantidad de gallos: "))
    K = int(input("Ingrese la cantidad de pollitos: "))
    Cantidad(N, M, K)
    print(f"La cantidad total en kilos de cane de las aves es de {Carne}")
```

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
def Valor(P, M, H):
    Valor_panes = 300*P
    Valor_leche = 3300*M
    Valor_Huevos = 350*H
    Valor_Total = Valor_panes + Valor_leche + Valor_Huevos
    global Vueltas
    Vueltas = B - Valor_Total


if __name__ == "__main__":
    P = int(input("Ingrese la cantidad de panes: "))
    M = int(input("Ingrese la cantidad de bolsas de leche: "))
    H = int(input("Ingrese la cantidad de huevos: "))
    B = int(input("Ingrese el valor del billete que le dieron: "))
    Valor(P, M, H)
    if Vueltas>0:
        print(f"Las vueltas que le quedan son {Vueltas}")
    elif Vueltas<0:
        print(f"Lo que quedo debiendo es {Vueltas}")
    else:
        print("No quedo debiendo nada")
```

5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

```python
def valor(C_inicial, I, N):
    C_final = C_inical*(1 + (I/100))**N
    return C_final

if __name__ == "__main__":
    C_inical = float(input("Ingrese el valor del prestamo: "))
    I = float(input("Ingrese el porcentaje del interes compuesto: "))
    N = int(input("Ingrese la cantidad de tiempo en meses: "))
    prestamo = valor(C_inical, I, N)
    print(f"El capital final es de {prestamo}")
```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
def contagiados(c, d):
    contagiados_totales = c*(2**d)
    return contagiados_totales

if __name__ == "__main__":
    contagiados_actuales = int(input("Ingrese la cantidad de contagiados actuales: "))
    dias = int(input("Ingrese la cantidad de dias que han pasado: "))
    total = contagiados(contagiados_actuales, dias)
    print(f"La cantidad de contagiados de covid-19 totales despues de {dias} dias es de {total}")
```

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```python
def promedio(N1, N2, N3, N4, N5):
    promedio = (N1 + N2 + N3 + N4 + N5)/5
    return promedio

def mediana(N1, N2, N3, N4, N5):
    numeros_ascendente = [N1, N2, N3, N4, N5]
    global orden_asc
    orden_asc = sorted(numeros_ascendente)
    mediana = (orden_asc)
    return mediana[2]

def promedio_multiplicativo(N1, N2, N3, N4, N5):
    promedio_multiplicativo = (N1 * N2 * N3 * N4 * N5)**(1/5)
    return promedio_multiplicativo

def numeros_ascendente(N1, N2, N3, N4, N5):
    return orden_asc

def numeros_descendente(N1, N2, N3, N4, N5):
    numeros_descendente = (N1, N2, N3, N4, N5)
    orden_des = sorted(numeros_descendente, reverse=True)
    return orden_des

def potencia(N1, N2, N3, N4, N5):
    mayor_numero = (orden_asc[4])
    menor_numero = (orden_asc[0])
    potencia = mayor_numero**menor_numero
    return potencia

def raiz(N1, N2, N3, N4, N5):
    menor_numero = (orden_asc[0])
    raiz = (menor_numero)**(1/3)
    return raiz

if __name__ == "__main__":
    N1 = float(input("Ingrese el primer numero real: "))
    N2 = float(input("Ingrese el segundo numero real: "))
    N3 = float(input("Ingrese el tecer numero real: "))
    N4 = float(input("Ingrese el cuarto numero real: "))
    N5 = float(input("Ingrese el quinto numero real: "))
    promedio_final = promedio(N1, N2, N3, N4, N5)
    mediana_final = mediana(N1, N2, N3, N4, N5)
    promedio_multiplicativo_final = promedio_multiplicativo(N1, N2, N3, N4, N5)
    numeros_asc_final = numeros_ascendente(N1, N2, N3, N4, N5)
    numeros_des_final = numeros_descendente(N1, N2, N3, N4, N5)
    potencia_final = potencia(N1, N2, N3, N4, N5)
    raiz_final = raiz(N1, N2, N3, N4, N5)

    print(f"De los cinco numeros, el promedio es {promedio_final}, la mediana es {mediana_final}, el promedio multiplicativo es {promedio_multiplicativo_final}")
    print(f"los numeros ordenados ascendentemente son {numeros_asc_final} y ordenados descendentemente son {numeros_des_final}")
    print(f"el mayor numero elevado a el menor numero es {potencia_final}, y la raiz cubica del menor numero es {raiz_final}")
```

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```python
#Se importan las funciones del archivo "funciones_inde"
from funciones_inde import *

if __name__ == "__main__":
    N1 = float(input("Ingrese el primer numero real: "))
    N2 = float(input("Ingrese el segundo numero real: "))
    N3 = float(input("Ingrese el tecer numero real: "))
    N4 = float(input("Ingrese el cuarto numero real: "))
    N5 = float(input("Ingrese el quinto numero real: "))
    promedio_final = promedio(N1, N2, N3, N4, N5)
    mediana_final = mediana(N1, N2, N3, N4, N5)
    promedio_multiplicativo_final = promedio_multiplicativo(N1, N2, N3, N4, N5)
    numeros_asc_final = numeros_ascendente(N1, N2, N3, N4, N5)
    numeros_des_final = numeros_descendente(N1, N2, N3, N4, N5)
    potencia_final = potencia(N1, N2, N3, N4, N5)
    raiz_final = raiz(N1, N2, N3, N4, N5)

    print(f"De los cinco numeros, el promedio es {promedio_final}, la mediana es {mediana_final}, el promedio multiplicativo es {promedio_multiplicativo_final}")
    print(f"los numeros ordenados ascendentemente son {numeros_asc_final} y ordenados descendentemente son {numeros_des_final}")
    print(f"el mayor numero elevado a el menor numero es {potencia_final}, y la raiz cubica del menor numero es {raiz_final}")
```

9. Consultar qué es y cómo funciona *pip* en python.



10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.
