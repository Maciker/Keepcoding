# Vamos a mostrar por pantalla las tablas de conversion de Celsius y Fahrenheit (multiplos de 10)
# C = (F-32) * 5/9
# F =

# Entrada de datos
def validar(frase):
    isStr=True
    while isStr:
        value = input(frase)
        if (value == 'c' or value == 'C' or value == 'f' or value == 'F'):
            isStr = False
    return value

def celsius(c):
    return round((c-32)*(5/9),2)

def fahrenheit(f):
    return round((f * (9/5)) + 32,2)


value = validar("Seleccione la tabla que desea ver, CElsius o Fahrenheit (c o f): ")

#Salida de datos

if value == 'c' or value == 'C':
    for i in range(230, -1, -10):
        print("El valor de", i,"en fahrenheit es :",fahrenheit(i))

if (value == 'f' or value == 'F'):
    for i in range(0, 231, 10):
        print("El valor de", i,"en celsius es :",celsius(i))
