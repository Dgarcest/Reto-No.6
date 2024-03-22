"""
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. 
Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
"""

def contagiados(c, d):
    contagiados_totales = c*(2**d)
    return contagiados_totales

if __name__ == "__main__":
    contagiados_actuales = int(input("Ingrese la cantidad de contagiados actuales: "))
    dias = int(input("Ingrese la cantidad de dias que han pasado: "))
    total = contagiados(contagiados_actuales, dias)
    print(f"La cantidad de contagiados de covid-19 totales despues de {dias} dias es de {total}")