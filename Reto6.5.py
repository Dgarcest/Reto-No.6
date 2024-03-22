#Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

def valor(C_inicial, I, N):
    C_final = C_inical*(1 + (I/100))**N
    return C_final

if __name__ == "__main__":
    C_inical = float(input("Ingrese el valor del prestamo: "))
    I = float(input("Ingrese el porcentaje del interes compuesto: "))
    N = int(input("Ingrese la cantidad de tiempo en meses: "))
    prestamo = valor(C_inical, I, N)
    print(f"El capital final es de {prestamo}")