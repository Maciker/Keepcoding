# Practica relacionada con la pelicula Marte
# como Matt Damon mandaba los mensajes.
base16 = ('1','2','3','4','5','6','7','8','9','a','b','c','e','f')
angulo=360/16
msg = "Hola"

for c in msg:
    c_hex = hex(ord(c))
    print(c_hex)
    hex_1 = c_hex[2]
    hex_2 = c_hex[3]
    print("Valores hexadecimales")
    print(hex_1)
    print(hex_2)
    #print("Valor del angulo")
    #print(base16.index(hex_1) * angulo)
    #print(base16.index(hex_2) * angulo)
    # Aqui algo no esta bien.
