import random
arr = []
defi = 0
bue = 0
reg = 0
exc = 0
for i in range(20):
	arr.append(int(random.randrange(20)))
	if arr[i] <= 5:
		defi += 1
	elif arr[i] <= 10 and arr[i] >= 6:
		reg += 1
	elif arr[i] <= 15 and arr[i] >= 11:
		bue += 1
	elif arr[i] <= 20 and arr[i] >= 16:
		exc +=1
print(arr)
print('Deficientes: ' + str(defi))
print('Regulares: ' + str(reg))
print('Buenos: ' + str(bue))
print('Excelentes: ' + str(exc))