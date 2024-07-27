dato = int(input("Ingrese un numero: "))
dato2 = int(input("Ingrese un numero: "))


if ((dato%2==0) and (dato2%2==0)):
    print("Ambos son pares")
elif ((dato%2==0) and (dato2%2!=0)):
    print(f"{dato} es par, {dato2} es impar")
elif ((dato%2!=0) and (dato2%2==0)):
       print(f"{dato2} es par {dato} es impar")
else:
     print("Ambos son impares")