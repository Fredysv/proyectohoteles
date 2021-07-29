seats = []
for i in range(4):
    seats.append([0]*8)


print(seats)
i=0
while i==0:
    
    opt=int(input("Digite 1 para reservar, 2 para mostrar todos los espacios, 3 para salir: "))
    if opt==1:
        hor=int(input("Digite el horario que quiere reservar: "))
        print(seats[hor])
        seat=int(input("Digite el asiento que desea reservar: "))
        if seats[hor][seat] == 1:
            print("Ya esta reservado")
        else:
            seats[hor][seat] = 1
            print("Campo reservado")
    elif opt==2:
        print(seats)
    elif opt==3:
        i=1
    else:
        print("digite una opcion correcta")