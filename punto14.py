import random as rd
def llenarA(n):
	for i in range(n):
		a.append(int(rd.randint(-100, 100)))

def llenarB(n):
	for i in range(n):
		b.append(int(rd.randint(-100, 100)))

def cSuma(a, b, n):
	temp = []
	for i in range(n):
		temp.append(int(a[i] + b[i]))
	return temp

def cResta(a, b, n):
	temp = []
	for i in range(n):
		temp.append(int(a[i] - b[i]))
	return temp


a = []
b = []
c = []
n = 0


while(True):
	print('1. Para llenar vector A de manera aleatoria')
	print('2. Para llenar vector B de manera aleatoria')
	print('3. Realizar C = A + B')
	print('4. Realizar C = B - A')
	print('5. Mostrar unos de los vectores')
	print('6. Salir')
	entrada = int(input(': '))
	if entrada == 1:
		if n == 0:
			n = int(input('Digite el tamaño del vector: '))
		llenarA(n)
	elif entrada == 2:
		if n == 0:
			n = int(input('Digite el tamaño del vector: '))
		llenarB(n)
	elif entrada == 3:
		if n == 0:
			print('Necesitas llenar los vectores')
		c = cSuma(a, b, n)
	elif entrada == 4:
		if n == 0:
			print('Necesitas llenar los vectores')
		c = cResta(a, b, n)
	elif entrada == 5:
		opc = int(input('1. Para mostrar A 2. Para mostrar B 3. Para mostrar C: '))
		if opc == 1:
			print(a)
		elif opc == 2:
			print(b)
		elif opc == 3:
			print(c)
	if entrada == 6:
		break