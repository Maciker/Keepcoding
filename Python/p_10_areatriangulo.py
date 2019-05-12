# Vamos a calcular el area de un triangulo

# Entrada de datos
def validar(frase):
    isint=False
    while not isint:
        strnum = input(frase)
        if (strnum.isdigit()):
            isint = True
    return strnum

def triangulo(b, h):
    return (b*h)/2

# Inputs los pasamos a int
base = round(float(validar("Teclea el valor de la base del triangulo ")),2)
altura = round(float(validar("Teclea el valo de la altura del triangulo ")),2)

#Salida de datos
print("El area del triangulo es:", triangulo(base, altura))