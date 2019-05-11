# La torutuga
# Importamos librera turtle para dibujar un cuadrado.
# Lo hacemos mediante una funcion para no repetir codigo.
# Ahora vamos a usar parametros y hacer que la funcion nos devuelva un valor.
import turtle

def cuadrado(lado):
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)

    return lado * lado

miT = turtle.Turtle()
cuadrado(50)
area01=cuadrado(50)
print("El area es: ", area01)
miT.left(90)
cuadrado(100)
area02=cuadrado(100)
print("El area es: ", area02)
miT.left(90)
cuadrado(25)
area03=cuadrado(25)
print("El area es: ", area03)
miT.left(90)
cuadrado(50)
area04=cuadrado(50)
print("El area es: ", area04)
miT.left(90)