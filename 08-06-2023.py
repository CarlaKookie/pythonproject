import numpy as np
#Importar la galeria par ahacer el arreglo, np es la abreviatura que le doy para no escribir numpy a cada rato

lista = [1,2,3,4,5]
print(lista) #Así se ve la lista

arreglo = np.array(lista) #Esto es para hacer el arreglo
print(arreglo) #Así se ve el arreglo

#ndim = Muestra las dimensiones del arreglo
print(arreglo.ndim)

#size = Muestra el largo del arreglo
print(arreglo.size)

#shape me muestra la forma del arreglo (filas, columnas,profundidad)
print(arreglo.shape)

#slice 
#[start:stop:step]
#[start::] = indico desde donde debo consultar la información
# [:Stop:] = Indica hasta donde debe usar datos
# []::Step] = Indica de cuanto en cuanto recorre los datos

print(arreglo[2::])
print(arreglo[1:3:])
print(arreglo[::-1]) #Los cuenta al reves, el negativo siempre es al reves aquí

#Formas de rellenar un array
#Con ciclo for:
arreglo2 = [i for i in range(1, 11)]
arreglo2 = np.array(arreglo2)
print(arreglo2)

# arange = Rellena arreglo con datos segun indicacion
# (Donde empiezo , donde termino - 1 , de cuanto en cuanto cuento)
arreglo3 = np.arange(1, 11)
print(arreglo3)

# Recorrido general usando arreglo como largo
#For each, x toma el valor de la posición o algo así entendí, no tengo contador, sirve más que nada cuando solo quiero recorrer el arreglo mas no deseo un contador
for x in arreglo2:
    print(x)

#for i, este es con contador parece
for i in range(10):
    print(arreglo2[1])

#Sumar valores al arreglo completo
arreglo3+=5
print(arreglo3)

#Multiplicar
arreglo3*=10
print(arreglo3)

#Arr3 es mayor a Arr2
print(arreglo3>arreglo2)



