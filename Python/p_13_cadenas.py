# Cadenas y codificacion
cadena = 'h o l a'
cadenaMayus = ''

for i in range(len(cadena)):
    print (cadena[i], " - ", ord(cadena[i]))
    # Vamos a ponerlo en mayusculas restando 32 al valor del caracter
    codigo=ord(cadena[i])-32
    cadenaMayus += chr(codigo)

print(cadenaMayus)

# Funcion que cuenta el numero de palabras de una frase.
def cuentaPalabras(cadena):
    frase = cadena.split()
    return len(frase)

cadena = 'Aqui hay cuatro palabras '
print (cadena, cuentaPalabras(cadena))



