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

#subproceso de guardar hotel en variable
hotel_puntarenas = ""
hotel_sancarlos = ""
hotel_guanacaste = ""
def save_hotel(hotel):
    global hotel_puntarenas
    global hotel_sancarlos
    global hotel_guanacaste
    if hotel[0] == 1:
        hotel_puntarenas = hotel
    if hotel[0] == 2:
        hotel_sancarlos = hotel
    if hotel[0] == 3:
        hotel_guanacaste = hotel
#termina subproceso para guardar hotel
#empieza subproceso para guardar clientes
clientes = []
first = 1
def save_client(cliente):
    global clientes
    global first
    if first == 1:
        clientes = cliente
        first = 0
    else:
        clientes.append(cliente)

#Empieza proceso de registrar hotel
def reg_hotel():
    hotel=[]
    for i in range(6):
        hotel.append("")
    #Los 3 hoteles disponibles
    print ("Hotel número 1: Puntarenas",
        "\nHotel número 2: San Carlos",
        "\nHotel número 3: Guanacaste")
    #solicitamos el nombre del hotel a trabajar
    hotel[0] = verificarnum(1,3,"Ingrese el número del hotel: ") #id del hotel
    if hotel[0] == 1:
        hotelname = str("Puntarenas")
    elif hotel[0] == 2:
        hotelname = str("San Carlos")
    elif hotel[0] ==3:
        hotelname = str("Guanacaste")
    print("Usted seleccionó el Hotel El Descanso "+hotelname+": ")
    #Pedimos los datos necesarios del
    hotel[1] = int(input("Digite la cantidad de habitaciones: ")) # Total de habitaciones
    hotel[2] = int(input("Digite la cantidad de personas por habitación: ")) #Huespedes por habitacion
    aforo = float(input("Indique el porcentaje de aforo aprobado: ")) #aforo aprobado
    hotel[3] = hotel[2] * hotel[1] *(aforo*0.01) # capacidad maxima de huespedes
    hotel[4] = 0 # cantidad de clientes actuales 
    hotel[5] = 0 # cantidad de habitaciones ocupadas

    save_hotel(hotel)# mandamos a guardar el hotel
#Termina registro hotel

#Empieza proceso de registro del Cliente
def reg_client():
    cliente = []
    for i in range(10):
        cliente.append("")
    cliente[0] = str(input("Digite su nombre completo: "))  # Nombre completo
    cliente[1] = str(input("Digite su número de identificación: ")) # ID
    cliente[2] = str(input("Ingrese su país de procedencia: ")) # Pais
    cliente[3] = str(input("Ingrese su provincia: ")) # Provincia
    cliente[4] = str(input("Ingrese su cantón: ")) # Canton
    cliente[5] = str(input("Ingrese su distrito: ")) # Distrito
    cliente[6] = str(input("Digite su dirección de residencia: ")) # Dirección
    cliente[7] = str(input("Digite su edad:")) # Edad
    cliente[8] = str(input("Elija su metodo de pago (efectivo, transferencia, tarjeta de crédito):")) # Metodo de pago
    cliente[9] = int(input("Cuantas personas lo van a acompañar?: ")) # Numero de acompañantes

    
    acomp = []  # Informacion de acompañantes
    #Guardamos la informacion de los acompañantes en un vector 
    for i in range(cliente[9]):
        acomp.append([""]*3)
    for i in range(cliente[9]):
        acomp[i][0] = str(input("Digite el nombre del acompañante {} : ".format(i+1)))
        acomp[i][1] = str(input("Digite la identificación del acompañante {} : ".format(i+1)))
        acomp[i][2] = str(input("Digite la edad del acompañante {} : ".format(i+1)))
    cliente.append(acomp)
    save_client(cliente)
    reg_reserv_hospe(cliente)

#Termina proceso de registro del Cliente

#Empieza Proceso registro de reservaciones de hospedaje
def reg_reserv_hospe(cliente):
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
    precio_dias = (diasentre*tari_entre+diasfinde*tari_finde)*(cliente[9]+1)
    print ("Precio neto: ",precio_dias)
    iva = precio_dias * 0.13
    print ("IVA: ",iva)
    precio_tot = precio_dias + iva
    print ("El precio total por dias selecionados es de: ",precio_tot)
#Termina Proceso de reservaciones de hospedaje

#Empieza Proceso registro de hoteles
rest1 = []
for i in range(7):
    rest1.append([0]*10)
rest2 = []
for i in range(7):
    rest2.append([0]*10)
rest3 = []
for i in range(7):
    rest3.append([0]*10)
def reserv_rest():
    global rest1
    global rest2
    global rest3
    #Los 3 restaurante disponibles
    print ("Restaurante número 1: Puntarenas",
            "\nRestaurante número 2: San Carlos",
        "\nRestaurante número 3: Guanacaste")
    #solicitamos el nombre del restaurante a trabajar
    rest = verificarnum(1,3,"Ingrese el número del restaurante: ") #id del restaurante
    if rest == 1:
        restname = str("Puntarenas")
    elif rest == 2:
        restname = str("San Carlos")
    elif rest ==3:
        restname = str("Guanacaste")
    print("Usted seleccionó el restaurante El Descanso "+restname+": ")
    print("Formato para los días que va a reservar:",
        "\nLunes = 1",
        "\nMartes = 2",
        "\nMiércoles = 3",
        "\nJueves = 4",
        "\nViernes = 5",
        "\nSábado = 6",
        "\nDomingo = 7")
    dia = (int(input("Ingrese el día a reservar: ")))-1
    print("Formato para los días que va a reservar:",
        "\nDesayuno",
        "\n7:00am = 1",
        "\n8:00am = 2",
        "\n9:00am = 3",
        "\n10:00am = 4",
        "\nAlmuerzo",
        "\n12:00md = 5",
        "\n1:00pm = 6",
        "\n2:00pm = 7"
        "\nCena",
        "\n7:00pm = 8"
        "\n8:00pm = 9"
        "\n9:00pm = 10")
    horario = (int(input("Ingrese el horario a reservar: ")))-1
    aforo = float(input("Indique el porcentaje de aforo aprobado: ")) #aforo aprobado
    maximo = 100 * (aforo*0.01)
    cantidad = int(input("Ingrese la cantidad de personas para el día a reservar: "))
    if rest == 1:
        if rest1[dia][horario]+cantidad > maximo:
            print("Su reservación excede el limite del aforo permitido, porfavor elija otro horario")
        else:
            rest1[dia][horario] += cantidad
    elif rest == 2 :
        if rest2[dia][horario]+cantidad > maximo:
            print("Su reservación excede el limite del aforo permitido, porfavor elija otro horario")
        else:
            rest2[dia][horario] += cantidad
    elif rest == 3 :
        if rest3[dia][horario]+cantidad > maximo:
            print("Su reservación excede el limite del aforo permitido, porfavor elija otro horario")
        else:
            rest3[dia][horario] += cantidad
    print(rest1,rest2,rest3)

#============= Programa Principal ================#
#=================================================#
print("Bienvenido a Hoteles el El Descanso")

#primero registramos al menos un hotel
reg_hotel()

exit = 0

#Menu Principal
while exit == 0:
    
    print(  "\nMenu",
            "\n1 = Sobreescribir Hotel o añadir", #por ahora solo será registro, en un futuro será añadir mas hoteles
            "\n2 = Registro de Nuevo Cliente",
            "\n3 = Reservacion restaurante",
            "\n4 = Salir")
    option = verificarnum(1,4,"Seleccione un numero de una opcion: ")
    if option == 1:
        reg_hotel()
    elif option == 2:
        reg_client()
    elif option == 3:
        reserv_rest()
    elif option == 4:
        exit =+ 1