#DEFINICION DE SUBPROCESOS


#subproceso para verificar numero
def verificarnum(a,b,text):
    num = 0
    while num == 0:
        num = int(input("{}".format(text)))
        if num > a-1 and num < b+1:
            return(num)
        else: 
            print("Digite un número valido: ")
            num = 0
#fin subproceso para verificar numeros

#Empieza proceso de registrar hotel
def reg_hotel():
    #Los 3 hoteles disponibles
    print ("Hotel número 1: Puntarenas",
        "\nHotel número 2: San Carlos",
        "\nHotel número 3: Guanacaste")
    #solicitamos el nombre del hotel a trabajar
    hotel_sel = verificarnum(1,3,"Ingrese el número del hotel: ")
    if hotel_sel == 1:
        hotel = str("Puntarenas")
    elif hotel_sel == 2:
        hotel = str("San Carlos")
    elif hotel_sel ==3:
        hotel = str("Guanacaste")
    print("Usted seleccionó el Hotel El Descanso "+hotel+": ")
    capacidadmax = int(input("Digite la capacidad maxima del hotel El Descanso "+hotel+": "))
    maxhabitaciones = int(input("Digite la cantidad de habitaciones que posee el hotel El Descanso "+hotel+": "))
    aforo = float(input("Indique el porcentaje de aforo aprobado para el hotel El Descanso "+hotel+": "))
    huespedesmax = int(capacidadmax / maxhabitaciones)
    capacidaddisp = int(capacidadmax * (aforo*0.01))
    habitacionesdisp = int(capacidaddisp / huespedesmax)
    print("\nEl hotel: El descanso",hotel,"cuenta con:"
        "\nEspacios habilitados: ",capacidaddisp,
        "\nHabitaciones Disponibles: ",habitacionesdisp)
#Termina registro hotel

#Empieza proceso de registro del Cliente
total_personas = 0
def reg_client():
    Nombre_client = str(input("Digite su nombre completo: "))
    id_client = str(input("Digite su número de identificación: "))
    pais = str(input("Ingrese su país de procedencia: "))
    provincia = str(input("Ingrese su provincia: "))
    canton = str(input("Ingrese su cantón: "))
    distrito = str(input("Ingrese su distrito: "))
    direccion = str(input("Digite su dirección de residencia: "))
    edad = str(input("Digite su edad:"))
    metodo_pago = str(input("Elija su metodo de pago (efectivo, transferencia, tarjeta de crédito):"))
    acomp_num = int(input("Cuantas personas lo van a acompañar?: "))
    global total_personas
    total_personas = 1+acomp_num
    
    i = 1
    j = acomp_num
    while i <= j:
        nombre_acomp = input("Digite el nombre del acompañante {} : ".format(i))
        id_acomp = input("Digite la identificación del acompañante {} : ".format(i))
        edad_acomp = input("Digite la edad del acompañante {} : ".format(i))
        i +=1
#Termina proceso de registro del Cliente

#Empieza Proceso registro de reservaciones de hospedaje
def reg_reserv_hospe():
    cant_dias = int(input("Cuantas días se va/n a hospedar?: "))
    i=1
    print("Formato para los días que se va a quedar:",
        "\nLunes = 1",
        "\nMartes = 2",
        "\nMiércoles = 3",
        "\nJueves = 4",
        "\nViernes = 5",
        "\nSábado = 6",
        "\nDomingo = 7")
    diasfinde = 0
    diasentre = 0
    for i in range(i,cant_dias+1):
        dias = int(input("Cual es el dia #{} que se va a quedar?: ".format(i)))
        if dias > 0 and dias < 6:
            diasentre +=1
        elif dias > 5 and dias < 8:
            diasfinde +=1
    tari_entre = int(input("Cual es la tarifa para dias entre semana: "))
    tari_finde = int(input("Cual es la tarifa para fines de semana: "))
    precio_dias = (diasentre*tari_entre+diasfinde*tari_finde)*total_personas
    print ("Precio neto: ",precio_dias)
    iva = precio_dias * 0.13
    print ("IVA: ",iva)
    precio_tot = precio_dias + iva
    print ("El precio total por dias selecionados es de: ",precio_tot)

#Termina Proceso de reservaciones de hospedaje


#============= Programa Principal ================#
#=================================================#
print("Bienvenido a Hoteles el El Descanso")

#primero registramos al menos un hotel
reg_hotel()


exit = 0

#Menu Princiapl
while exit == 0:
    
    print(  "\nMenu",
            "\n1 = Sobreescribir Hotel o añadir", #por ahora solo será registro, en un futuro será añadir mas hoteles
            "\n2 = Registro de Cliente",
            "\n3 = Salir")
    option = verificarnum(1,3,"Seleccione un numero de una opcion: ")
    if option == 1:
        reg_hotel()
    elif option == 2:
        reg_client()
        reg_reserv_hospe()
    elif option == 3:
        exit =+ 1