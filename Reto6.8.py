#Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

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