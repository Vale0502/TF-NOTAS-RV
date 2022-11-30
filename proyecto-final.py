import pandas as pd

canAlumnos = 10;
canExamenes = 5;
matrizNotas = []

titulosArriba = []
titulosIzquierda = []

#Ingresando notas de alumnos
for n in range(canAlumnos):
    matrizNotas.append([])
    for m in range(canExamenes):
        matrizNotas[n].append(int(input('Introducir notas del examen ' + str(m + 1)  + ' del estudiante ' + str(n + 1) + ': ')))

filas = len(matrizNotas)
columnas = len(matrizNotas[0])

for i in range(filas):
    promAlu = round(sum(matrizNotas[i])/canExamenes,2)
    matrizNotas[i].append(promAlu)
    
nueva_fila = []

for j in range(columnas):
    promExa = round(sum([fila[j] for fila in matrizNotas])/canAlumnos,2)
    nueva_fila.append(promExa)

print(nueva_fila)

for n in range(canAlumnos):
    titulosIzquierda.append('Alumno ' + str(n + 1))
    
for m in range(canExamenes):
    titulosArriba.append('Examen ' + str(m + 1))

titulosArriba.append('Promedio')

print('#################################################')
print('################## T A B L A ####################')
print('#################################################')

nueva_fila.append('-')

df = pd.DataFrame(matrizNotas, columns = titulosArriba, index = titulosIzquierda)
df.loc['Resumen'] = nueva_fila
print(df)
print('#################################################')