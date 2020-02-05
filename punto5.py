arr = []
tam_arr = int(input('Digite el tamaño del arreglo: '))
num = int(input('Digite  un numero: '))
arr.append(num)
for i in range(tam_arr - 1):
    arr.append(num * (i+2))
print(arr)

