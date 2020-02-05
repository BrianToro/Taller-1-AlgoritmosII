tam_arr = int(input('Ingrese el tamaño del array: '))
arr = []
for i in range(tam_arr):
    temp = int(input('Agrega un numero al array: '))
    if temp not in arr:
        arr.append(temp)
print(arr)