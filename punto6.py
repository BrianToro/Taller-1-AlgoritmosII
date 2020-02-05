arr_names = []
arr_len = []
tam_arr = int(input('Digite el tamaño del arreglo: '))

for i in range(tam_arr):
    arr_names.append(input('Digite el ' + str(i + 1) + ' nombre: '))
    arr_len.append(len(arr_names[i]))
print(arr_names)
print(arr_len)