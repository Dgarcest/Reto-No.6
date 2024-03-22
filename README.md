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
    print(f"El volumen de la esfera es de {Volumen_esfera} y el del cono el de {Volumen_cono}")
    print(f"La superficie de la esfera es de {Superficie_esfera} y la del cono el de {Superficie_cono}")
```

2. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="800" height="auto"/></br>
</div>

* Una función matemática para calcular el área y el perimetro.
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
* Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

9. Consultar qué es y cómo funciona *pip* en python.

10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.
