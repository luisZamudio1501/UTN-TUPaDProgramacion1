# de una semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [10, 20], #domingo
    [9, 18], #lunes
    [11, 19], #martes
    [8, 22], #miercoles
    [10, 23], #jueves
    [11, 24], #viernes
    [10, 25], #sabado
    ]
    
suma_min = 0
suma_max = 0
 
for i in range(len(temperaturas)):
    suma_min += temperaturas[i][0]
    suma_max += temperaturas[i][1]

promedio_min = suma_min / 7
promedio_max = suma_max / 7

dias_semana = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
amplitud_max = 0 
dia_amp_max = ""

for i in range(len(temperaturas)):
    aux = temperaturas[i][1] - temperaturas[i][0]
    if aux > amplitud_max:
        amplitud_max = aux
        dia_amp_max = dias_semana[i]

print(f"El promedio de temperaturas mínimas es {promedio_min:.2f}° C")
print(f"El promedio de temperaturas máximas es {promedio_max:.2f}° C")

print(f"La mayor amplitud térmica se resgistró el día {dia_amp_max} con {amplitud_max}° C")





