#Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

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