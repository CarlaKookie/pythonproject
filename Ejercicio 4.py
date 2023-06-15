#Crear una lista con 20 números enteros aleatorios entre 1 y 100. Luego muestre la lista.
import random
lista=[]
for i in range (20):
    lista.append(random.randint(1,100))
print(lista)
lista.sort()
print(lista)