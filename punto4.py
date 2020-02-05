import random
arr =  []
for i in range(10):
    arr.append(random.randrange(100))
print("El arreglo es: "  + str(arr) + ", el numero mayor es: " + str(max(arr)) + " y el numero menor es: " + str(min(arr)))  