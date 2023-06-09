import numpy as np
arregloA = np.random.randint(0,500,(100))
print(arregloA)
for i in range(arregloA.size):
    if i%2==0:
        print(arregloA[i])