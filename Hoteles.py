import os
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

#subproceso para convertir row de array en una linea para guardar
def compile_row_string(hotel):
        return str(hotel).strip(']').strip('[').replace(' ','')
#fin subproceso para convertir row de array en una linea para guardar

#subproceso de guardar hotel en variable
Hotel_info = []
Hotel_name = ""
def save_hotel(hotel):
    global Hotel_info
    global Hotel_name
    Hotel_info = hotel
    if hotel[0] == 1:
        file=open("Hotel_puntarenas.txt", "w")
        for row in hotel:
            file.write(compile_row_string(row)+'\n')
        file.close()
        Hotel_name = "Puntarenas"
    if hotel[0] == 2:
        file=open("Hotel_sancarlos.txt", "w")
        for row in hotel:
            file.write(compile_row_string(row)+'\n')
        file.close() 
        Hotel_name = "San Carlos"
    if hotel[0] == 3:
        file=open("Hotel_guanacaste.txt", "w")
        for row in hotel:
            file.write(compile_row_string(row)+'\n')
        file.close()
        Hotel_name = "Guanacaste"
    print(Hotel_info)
#termina subproceso para guardar hotel

#Empieza proceso para agarrar un hotel ya existente
def get_hotel():
    global Hotel_info
    global Hotel_name
    print('Seleccione uno de los hoteles disponibles: ')
    if os.path.isfile('Hotel_puntarenas.txt'):
        print('Hotel número 1: Puntarenas')
    if os.path.isfile('Hotel_sancarlos.txt'):
        print("\nHotel número 2: San Carlos")
    if os.path.isfile('Hotel_guanacaste.txt'):
        print("\nHotel número 3: Guanacaste")
    opt = verificarnum(1,3,"Seleccione: ")
    if opt == 1:
        file=open("Hotel_puntarenas.txt", "r")
        Hotel_info = [(line.strip()) for line in file]
        file.close()
        Hotel_name = "Puntarenas"
    if opt == 2:
        file=open("Hotel_sancarlos.txt", "r")
        Hotel_info = [(line.strip()) for line in file]
        file.close()
        Hotel_name = "San Carlos"
    if opt == 3:
        file=open("Hotel_guanacaste.txt", "r")
        Hotel_info = [(line.strip()) for line in file]
        file.close()
        Hotel_name = "Guanacaste"
#Termina proceso para agarrar un hotel ya existente

#Empieza proceso de registrar hotel
def reg_hotel():
    hotel=[]
    for i in range(6):
        hotel.append("")
    #Los 3 hoteles disponibles
    print (   "----------------------------"
            "\n|Hotel número 1: Puntarenas|",
            "\n|Hotel número 2: San Carlos|",
            "\n|Hotel número 3: Guanacaste|"
            "\n----------------------------")
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

#Empieza proceso para agarrar los clientes ya existentes
def get_clientes():
    global clientes
    file=open('clientes.txt', "r")
    clientes = [(line.strip()).split() for line in file]
    file.close()
#Termina proceso para agarrar un hotel ya existente

#empieza subproceso para guardar clientes
clientes = []
def save_client(cliente):
    global clientes
    if not os.path.isfile('clientes.txt'):
        clientes = cliente
        file=open('clientes.txt', "w")
        for row in cliente:
            file.write(compile_row_string(row)+' ')
        file.close()
    else:
        clientes.append(cliente)
        file=open("clientes.txt", "a")
        file.write('\n')
        for row in cliente:
            file.write(compile_row_string(row)+' ')
        file.close()
        get_clientes()
#termina subproceso para guardar clientes

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
    save_client(cliente)
    reg_reserv_hospe(cliente)

#Termina proceso de registro del Cliente

#Empieza Proceso registro de reservaciones de hospedaje
def reg_reserv_hospe(cliente):
    cant_dias = int(input("Cuantas días se va/n a hospedar?: "))
    i=1
    print("----------------------------------------------",
        "\n| Formato para los días que se va a quedar:  |",
        "\n| Lunes = 1                                  |",
        "\n| Martes = 2                                 |",
        "\n| Miércoles = 3                              |",
        "\n| Jueves = 4                                 |",
        "\n| Viernes = 5                                |",
        "\n| Sábado = 6                                 |",
        "\n| Domingo = 7                                |",
        "\n----------------------------------------------")
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

#variables de restaurante
rest1 = []
for i in range(7):
    rest1.append([0]*10)
rest2 = []
for i in range(7):
    rest2.append([0]*10)
rest3 = []
for i in range(7):
    rest3.append([0]*10)

#empieza proceso agarrar restaurantes existentes
def get_rest():
    global rest1
    global rest2
    global rest3
    if os.path.isfile('rest1.txt') and os.path.isfile('rest2.txt') and os.path.isfile('rest3.txt'):
        file=open('rest1.txt', "r")
        rest1 = [(line.strip()).split() for line in file]
        file.close()
        file=open('rest2.txt', "r")
        rest2 = [(line.strip()).split() for line in file]
        file.close()
        file=open('rest3.txt', "r")
        rest3 = [(line.strip()).split() for line in file]
        file.close()
        for i in range(7):
            for j in range(10):
                rest1[i][j] = int(rest1[i][j])
        for i in range(7):
            for j in range(10):
                rest2[i][j] = int(rest2[i][j])
        for i in range(7):
            for j in range(10):
                rest3[i][j] = int(rest3[i][j])
#Termina proceso para agarrar un hotel ya existente

#empieza subproceso para guardar restaurantes
def save_rest(a,b,c):
    global rest1
    global rest2
    global rest3
    rest_1 = a
    rest_2 = b
    rest_3 = c
    file=open('rest1.txt', "w")
    for row in rest_1:
        for rest_1 in row:
            file.write(compile_row_string(rest_1)+' ')
        file.write("\n")
    file.close()
    file=open('rest2.txt', "w")
    for row in rest_2:
        for rest_2 in row:
            file.write(compile_row_string(rest_2)+' ')
        file.write("\n")
    file.close()
    file=open('rest3.txt', "w")
    for row in rest_3:
        for rest_3 in row:
            file.write(compile_row_string(rest_3)+' ')
        file.write("\n")
    file.close()
#termina subproceso para guardar restaurantes

#Empieza reservacion rest

def reserv_rest():
    global rest1
    global rest2
    global rest3
    #Los 3 restaurante disponibles
    print (   "----------------------------"
            "\n|Hotel número 1: Puntarenas|",
            "\n|Hotel número 2: San Carlos|",
            "\n|Hotel número 3: Guanacaste|"
            "\n----------------------------")
    #solicitamos el nombre del restaurante a trabajar
    rest = verificarnum(1,3,"Ingrese el número del restaurante: ") #id del restaurante
    if rest == 1:
        restname = str("Puntarenas")
    elif rest == 2:
        restname = str("San Carlos")
    elif rest ==3:
        restname = str("Guanacaste")
    print("Usted seleccionó el restaurante El Descanso "+restname+": ")
    print("------------------------------------------------",
        "\n| Formato para los días que va a reservar      |",
        "\n| Lunes = 1                                    |",
        "\n| Martes = 2                                   |",
        "\n| Miércoles = 3                                |",
        "\n| Jueves = 4                                   |",
        "\n| Viernes = 5                                  |",
        "\n| Sábado = 6                                   |",
        "\n| Domingo =  7                                 |",
        "\n------------------------------------------------")
    dia = (int(input("Ingrese el día a reservar: ")))-1
    print("---------------------------------------------"
        "\n| Formato para las horas que va a reservar: |",
        "\n| Desayuno                                  |",
        "\n| 7:00am = 1                                |",
        "\n| 8:00am = 2                                |",
        "\n| 9:00am = 3                                |",
        "\n| 10:00am = 4                               |",
        "\n| Almuerzo                                  |",
        "\n| 12:00md = 5                               |",
        "\n| 1:00pm = 6                                |",
        "\n| 2:00pm = 7                                |"
        "\n| Cena                                      |",
        "\n| 7:00pm = 8                                |"
        "\n| 8:00pm = 9                                |",
        "\n| 9:00pm = 10                               |",
        "\n---------------------------------------------")
    horario = (int(input("Ingrese el horario a reservar: ")))-1
    aforo = float(input("Indique el porcentaje de aforo aprobado: ")) #aforo aprobado
    maximo = 100 * (aforo*0.01)
    cantidad = int(input("Ingrese la cantidad de personas para el día a reservar: "))
    get_rest()
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
    save_rest(rest1,rest2,rest3)
#Termina Proceso de reservaciones de restaurante

#Empieza Check In y Check Out
def check():
    check= 0
    check= (int(input("Ingrese código de Check In =1 ó Check Out =2: ")))
    if check == 1:
        hotel1 = []
        for i in range(7):
            hotel1.append([0]*6)
        hotel2 = []
        for i in range(7):
            hotel2.append([0]*6)
        hotel3 = []
        for i in range(7):
            hotel3.append([0]*6)
    elif check == 2:
        hotel1 = []
        for i in range(7):
            hotel1.append([0]*5)
        hotel2 = []
        for i in range(7):
            hotel2.append([0]*5)
        hotel3 = []
        for i in range(7):
            hotel3.append([0]*5)

    #Los 3 Hotel disponibles
    print (   "----------------------------"
            "\n|Hotel número 1: Puntarenas|",
            "\n|Hotel número 2: San Carlos|",
            "\n|Hotel número 3: Guanacaste|"
            "\n----------------------------")
    #solicitamos el nombre del Hotel a trabajar
    hot = verificarnum(1,3,"Ingrese el número del Hotel: ") #id del Hotel
    if hot == 1:
        hotelname = str("Puntarenas")
    elif hot == 2:
        hotelname = str("San Carlos")
    elif hot ==3:
        hotelname = str("Guanacaste")
    print("Usted seleccionó el Hotel El Descanso "+hotelname+": ")
    print("------------------------------------------------",
        "\n| Formato para los días Check In o Check Out:  |",
        "\n| Lunes = 1                                    |",
        "\n| Martes = 2                                   |",
        "\n| Miércoles = 3                                |",
        "\n| Jueves = 4                                   |",
        "\n| Viernes = 5                                  |",
        "\n| Sábado = 6                                   |",
        "\n| Domingo =  7                                 |",
        "\n------------------------------------------------")
    dia = (int(input("Ingrese el día de Check In o Check Out: ")))-1
    print("----------------------------------------------------------"
        "\n| Formato para los horarios de Check In o Check Out:     |",
        "\n| Check In                                               |",
        "\n| 2:00pm = 1                                             |",
        "\n| 2:30pm = 2                                             |",
        "\n| 3:00pm = 3                                             |",
        "\n| 3:30pm = 4                                             |",
        "\n| 4:00pm = 5                                             |",
        "\n| 4:30pm = 6                                             |",
        "\n| Check Out                                              |",
        "\n| 11:30am = 1                                            |",
        "\n| 12:00pm = 2                                            |",
        "\n| 12:30pm = 3                                            |",
        "\n| 1:00pm = 4                                             |",
        "\n| 1:30pm = 5                                             |",
        "\n----------------------------------------------------------")
    horario = (int(input("Ingrese el horario : ")))-1
    maximo = 20
    cantidad = 1
    print("Unicamente una persona por Check in o Check Out")
    if hot == 1:
        if hotel1[dia][horario]+cantidad > maximo:
            print("Su reservación excede el limite del aforo permitido, porfavor elija otro horario")
        else:
            hotel1[dia][horario] += cantidad
    elif hot == 2 :
        if hotel2[dia][horario]+cantidad > maximo:
            print("Su reservación excede el limite del aforo permitido, porfavor elija otro horario")
        else:
            hotel2[dia][horario] += cantidad
    elif hot == 3 :
        if hotel3[dia][horario]+cantidad > maximo:
            print("Su reservación excede el limite del aforo permitido, porfavor elija otro horario")
        else:
            hotel3[dia][horario] += cantidad
    print(hotel1)
    print(hotel2)
    print(hotel3)
#Termina Proceso de Check In y Check Out '''


#============= Programa Principal ================#
#=================================================#
print("Bienvenido a Hoteles el El Descanso")

#primero registramos si no hay archivo plano
if os.path.isfile('Hotel_puntarenas.txt') or os.path.isfile('Hotel_sancarlos.txt') or os.path.isfile('Hotel_guanacaste.txtxt'):
    get_hotel()
else:
    reg_hotel()
exit = 0
#Menu Principal
while exit == 0:
    
    print("------------------------------------------------",
        "\n| Menu                                         |",                                       
        "\n  Hotel Selecionado actualmente= {}            ".format(Hotel_name),
        "\n| 1 = Seleccionar otro hotel                   |",
        "\n| 2 = Sobreescribir Hotel o añadir otro        |",
        "\n| 3 = Registro de Nuevo Cliente                |",
        "\n| 4 = Reservacion restaurante                  |",
        "\n| 5 = Check in - Check                         |",
        "\n| 6 = Salir                                    |",
        "\n------------------------------------------------")

    option = verificarnum(1,6,"Seleccione un numero de una opcion: ")
    if option == 1:
        get_hotel()
    elif option == 2:
        reg_hotel()
    elif option == 3:
        reg_client()
    elif option == 4:
        reserv_rest()
    elif option == 5:
        check()
    elif option == 6:
        exit =+ 1