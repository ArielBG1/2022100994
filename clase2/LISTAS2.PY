array=["Futbol","pc",18.6,18,[6,7,10.4],True,False,"pc"]
array2=[200,250,"hola"]
array3=array+array2
print(array)
#Buscar valores
print("pc" in array)
#saber el indice dpnde esta lo que se busca
print(array.index("pc"))
#cantidad de veces que tengo el valor enmi array
print(array.count("pc"))
#Borrar
array.remove("pc")
print(array)
#limpiar
#array.clear()
print(array)
#cambiar posiciones
array.reverse()
print(array)
#ordenar de mayor a menor
array4=[1,2,8,-11,5]
array4.sort()
print(array4)
