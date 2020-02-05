arr_names = ['Andres',  'Pedro', 'Juliana', 'Juan', 'Fernando', 'Camila', 'Maria', 'Catalina', 'Jose', 'Charlie']
name_search = str(input('Digite un nombre: '))
if name_search in arr_names:
    print('El nombre ' +  str(name_search) + ' esta en la posicion: ' + str(arr_names.index(name_search)) + ' del arreglo')
else:
    print('No se encuentra el nombre ' + str(name_search) + ' en el arreglo')
