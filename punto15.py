import math
billetes = [100000, 50000, 20000, 10000, 5000, 2000]
monedas = [1000, 500, 200, 100, 50]

entrada = int(input('Digite la cantidad de dinero que necesita: '))

lista = []
num_bill = 0
num_mon = 0
num_pros = entrada

while num_pros >= 50:
	for billete in billetes:
		if num_pros / billete >= 1:
			cantbill = math.floor(num_pros/billete)
			num_pros -= cantbill*billete
			num_bill += 1
			lista.append(int(billete))

	for moneda in monedas:
		if num_pros / moneda >= 1:
			cantmon = math.floor(num_pros/moneda)
			num_pros -= cantmon*moneda
			num_mon += 1
			lista.append(int(moneda))

print('Cantidad de billetes: ' + str(num_bill))
print('Cantidad de monedas: ' + str(num_mon))
print(lista)

