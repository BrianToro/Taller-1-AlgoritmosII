arr1 = []
arr2  = []
arr3 = []

for i in range(5):
    arr1.append(int(input('Digite un numero para la posicion ' + str(i) + ' del 1er arreglo: ')))
    arr2.append(int(input('Digite un numero para la posicion ' + str(i) + ' del 2do arreglo: ')))
    arr3.append(int(arr1[i] + arr2[i]))

print(arr1, arr2, arr3)