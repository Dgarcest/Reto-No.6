"""
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
El promedio
La mediana
El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
Ordenar los números de forma ascendente
Ordenar los números de forma descendente
La potencia del mayor número elevado al menor número
La raíz cúbica del menor número
"""

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