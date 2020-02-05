alum_alg = []
alum_an = []
alum_rep = []

for i in range(10):
    alum_alg.append(input('Digite el id del alumno ' + str(i+1) + ' de  algebra'))
    alum_an.append(input('Digite el id del alumno ' + str(i+1) + ' de  analisis'))
    if alum_alg[i] in alum_an and alum_alg[i] not in alum_rep:
        alum_rep.append(alum_alg[i])
    elif alum_an[i] in alum_alg and alum_an[i] not in alum_rep:
         alum_rep.append(alum_an[i])

print('El id de los alumnos repetidos es: ' +  str(alum_rep)  + ' total: ' + str(len(alum_rep)))
