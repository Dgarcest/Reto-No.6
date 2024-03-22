"""
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. 
Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
"""

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