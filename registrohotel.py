#Proyecto Final - Intro Progra
#Modulo 01
'''Instrucciones: Solicitar nombre del hotel, capacidad total, cantidad de habitaciones, 
aforo aprobado y calcular la cantidad de habitaciones y espacios que se pueden habilitar
para reservar para cada día de la semana (lunes a domingo).'''


hotel = str(input("Ingrese el nombre del hotel: "))
capacidadmax = int(input("Digite la capacidad maxima del hotel: "))
maxhabitaciones = int(input("Digite la cantidad de habitaciones que posee el hotel: "))
aforo = float(input("Indique el porcentaje de aforo aprobado: "))


huespedesmax = int(capacidadmax / maxhabitaciones)
capacidaddisp = int(capacidadmax * (aforo*0.01))
habitacionesdisp = int(capacidaddisp / huespedesmax)

print("\nEl hotel: El descanso-",hotel,"cuenta con:"
    "\nEspacios habilitados: ",capacidaddisp,
    "\nHabitaciones Disponibles: ",habitacionesdisp)