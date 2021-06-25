'''Proyecto Final - Intro Programación.
Módulo #2: Solicitar nombre del cliente, número de identificación, país, provincia, cantón, distrito
y otras especificaciones de dirección, edad, forma de pago (efectivo, transferencia, tarjeta de crédito)
Solicitar cuántas personas lo acompañan y de acuerdo con este número solicitar nombre, número de 
identificación, edad de cada una de ellas.'''

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

i = 1
j = acomp_num
while i <= j:
    nombre_acomp = input("Digite el nombre del acompañante {} : ".format(i))
    id_acomp = input("Digite la identificación del acompañante {} : ".format(i))
    edad_acomp = input("Digite la edad del acompañante {} : ".format(i))
    i +=1