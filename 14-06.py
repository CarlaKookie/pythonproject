lista = []
n=0
suma=0
prom=0
for i in range (10):
    n=int(input("Ingrese un número a la lista: "))
    lista.append(n)
    suma+=n
    prom=suma/10
print(f"La suma es: {suma} y el promedio es {prom}")
