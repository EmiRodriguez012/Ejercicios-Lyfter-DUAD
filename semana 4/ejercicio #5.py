total_notas= 0
notas_aprobadas= 0
notas_desaprobadas= 0
promedio_aprobadas= 0
promedio_desaprobadas= 0
promedio_total= 0
nota_ingresada= 0
contador_nota= 0
suma_desaprobadas= 0
suma_aprobadas= 0
suma_notas= 0



total_notas= int(input("Porfavor ingrese su total de notas: "))

while ( contador_nota != total_notas):
    contador_nota = contador_nota + 1
    nota_ingresada = int(input(f"Ingrese la nota numero:  {contador_nota}: "))
    if (nota_ingresada < 70):
        notas_desaprobadas = notas_desaprobadas + 1
        suma_desaprobadas = suma_desaprobadas + nota_ingresada 
    
    else:
        notas_aprobadas = notas_aprobadas + 1
        suma_aprobadas = suma_aprobadas + nota_ingresada

if (notas_aprobadas > 0):
    promedio_aprobadas = suma_aprobadas / notas_aprobadas
if (notas_desaprobadas > 0):
    promedio_desaprobadas = suma_desaprobadas / notas_aprobadas


suma_notas= suma_aprobadas + suma_desaprobadas
promedio_total=  suma_notas / total_notas



print(f"El estudiante tiene esta cantidad de notas aprobadas: {notas_aprobadas}")

print(f"El estudiante tiene esta cantidad de notas desaprobadas: {notas_desaprobadas}")

print(f"El estudiante tiene este promedio de notas aprobadas: {promedio_aprobadas}")

print(f"El estudiante tiene este promedio de notas desaprodas: {promedio_desaprobadas}")

print(f"El estudiante tiene este promedio total de notas: {promedio_total}")
