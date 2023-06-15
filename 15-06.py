def saludo ():
    print("HOLAAAAAAAAAAAAAAAA")

#saludo()

def sumar():
    num1=3
    num2=5
    return(num1+num2)
#print("La suma es ", sumar())

def suma(a,b):
    suma=a+b
    print(f"La suma de los argumetos es {suma}")

#num1= int(input("Ingrese el primer número: "))
#num2= int(input("Ingrese el segundo número: "))
#suma(num1,num2)

def suma(a,b):
    suma=a+b
    return(suma)

#num1= int(input("Ingrese el primer número: "))
#num2= int(input("Ingrese el segundo número: "))
#print("El resultado de la suma es", suma(num1,num2))

lista = [10,90,100,500,1000,5000]
#Sin argumeto sin retoro
#Que muestre todos losvalores de la lista (uno por uno)
def listar():
    for i in range(len(lista)):
        print(lista[i])
#listar()

def buscar(valor):
    res="No se encuentra"
    for x in lista:
        if x == valor:
            res="Valor existe"
    print(res)
#num=int(input("Ingrese valor a buscar "))
#buscar(num)

#Eliminar un registro de la lista
def eliminar(valor):
    try:
         lista.remove(valor)
         print("Eliminado con exito")
    except ValueError:
        print("Valor no se encuetra en la lista.")

num =int(input("Ingrese un valor: "))
eliminar(num)