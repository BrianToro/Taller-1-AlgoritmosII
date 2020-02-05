import random, math
while(True):
    n = int(input('Ingrese la cantidad de n (Debe  ser un numero  impar): '))
    if n%2 != 0:
        break
arr = []
for i in range(n):
    arr.append(random.randrange(100))

print(arr)
print('El numero de enmedio es:  ' + str(arr[math.ceil(len(arr)/2) - 1]))