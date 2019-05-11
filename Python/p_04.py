# Trabajando con numeros.
# Introduce dos numeros enteros. El programa los divide por 10, redondea a 2 y hace 4 operaciones: + - * /

# Entrada de datos
isint=False
while not isint:
    strnum01 = input("Teclea el primer numero: ")
    if (strnum01.isdigit() or (strnum01[0]=='-' and strnum01[1:].isdigit())):
        isint = True

isint=False
while not isint:
    strnum02 = input("Teclea el segundo numero: ")
    if (strnum02.isdigit()or (strnum02[0]=='-' and strnum02[1:].isdigit())):
        isint = True

# Inputs los pasamos a int
num01 = round(int(strnum01)/10,2)
num02 = round(int(strnum02)/10,2)

#Salida de datos
print("La suma de ", num01," y ", num02," es: ", round(num01 + num02,2))
print("La resta de ", num01," y ", num02," es: ", round(num01 - num02,2))
print("La division de ", num01," y ", num02," es: ", round(num01 / num02,2))
print("La multiplicacion de ", num01," y ", num02," es: ", round(num01 * num02,2))
