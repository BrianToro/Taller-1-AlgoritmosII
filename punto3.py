import random
arr =  []
for i in range(10):
    arr.append(random.randrange(100))
print("El arreglo es: "  + str(arr) + " y su promedio es: " + str(sum(arr)/len(arr)))