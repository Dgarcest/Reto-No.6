#Archivo de funciones

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