array=["Futbol","pc",18.6,18,[6,7,10.4],True,False]
print(array)
print(array[1])
print(array[4])
print(array[-1])
print(array[0:3])
print(array[:2])
print(array[2:])
#CANTIDAD DE DATOS

print(len(array))

#AGREGAR UN VALOR

array.append(66)
print(array)
#INSERTAR DATOS EN UNA POSICION

array.insert(1,88)
print(array)
#INSERTAR MAS DE UN DATO AL FINAL

array.extend([1,88,True,100])
print(array)