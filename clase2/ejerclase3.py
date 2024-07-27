def ingresar():
    numeros = []
    while True:
        numero = input("Ingrese un numero, n para terminar: ")
        if numero.lower() == 'n':
            break
        numeros.append(float(numero))
    return numeros

def sumar 


def main():
    numeros = ingresar()
    if len(numeros) == 0:
        print("No se ingresaron numeros")
        return
    suma = sumar(numeros)
    promedio = promedio(numeros)
    maximo, minimo= encontrar_max_min(numeros)
    mayores = numeros_mayores_prom(numeros,promedio)

    print(f"Numeros Ingresados: {numeros}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Num grande: {maximo}")
    print(f"Num Pequeño: {minimo}")
    print(f"Numeros mayores que el promedio: {mayores}")
    if __name__ == "__main__":
        main()