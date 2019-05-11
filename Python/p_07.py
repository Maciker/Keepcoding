# Trabajando con numeros.
# Introduce dos numeros enteros. El programa los divide por 10, redondea a 2 y hace 4 operaciones: + - * /
# Vamos a utilizar una funcion para validar la entrada de datos

# Entrada de datos
def validar():
    isint=False
    while not isint:
        strnum = input("Teclea un numero entero: ")
        if (strnum.isdigit() or (strnum[0]=='-' and strnum[1:].isdigit())):
            isint = True
    return strnum

# Inputs los pasamos a int
num01 = round(int(validar())/10,2)
num02 = round(int(validar())/10,2)

#Salida de datos
print("La suma de ", num01," y ", num02," es: ", round(num01 + num02,2))
print("La resta de ", num01," y ", num02," es: ", round(num01 - num02,2))
print("La division de ", num01," y ", num02," es: ", round(num01 / num02,2))
print("La multiplicacion de ", num01," y ", num02," es: ", round(num01 * num02,2))