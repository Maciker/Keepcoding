# Determinar el precio de X entradas para un grupo de personas que entra al Zoo
def calcularPrecioEntrada(e):
    if e > 0 and e <= 2:
        return 0
    elif e <= 12:
        return 14
    elif e < 65:
        return 23
    else:
        return 18

def validarEdad(cadena):
    try:
        n = int(cadena)
        if n >= 0:
            return True
        return False
    except:
        return False

def pedirEdad():
    control = False
    while not control:
        edad = input("¿Que edad tienes? ")
        control = validarEdad(edad)
    return int(edad) #Validar entrada

edad = pedirEdad()
precioTotal = 0

while edad != 0:
    precioTotal += calcularPrecioEntrada(edad)
    print("El precio de la entrada es: ",calcularPrecioEntrada(edad))

    edad = pedirEdad()

print('El precio total de las entradas es: ', precioTotal)