cant = int(input('Digite el numero de notas: '))
notas = []
n_apro = 0
n_desa = 0
desa = 0
apro = 0
for i in range(cant):
	notas.append(int(input('Agregue la ' + str(i+1) + ' nota: ')))
	if notas[i] < 3:
		desa += 1
		n_desa += notas[i]
	else:
		apro += 1
		n_apro += notas[i]

print('El promedio de aprobados es: ' + str(n_apro/apro) + ' y el numero de aprobados es: ' + str(apro))
print('El promedio de desaprobados es: ' + str(n_desa/desa) + ' y el numero de desaprobados es: ' + str(desa))