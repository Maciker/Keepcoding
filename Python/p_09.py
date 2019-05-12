# Calcular la media
# Gestion de excepciones en Python

# Ejemplo try - except
lista = (1,2,3,4)
try:
    print (lista[4])
except:
    print ("Fuera de rango")

# Haremos la media de esta lista
notas = (2,4,6,8)

def contenido(lista, indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    return resultado

i = 0
suma = 0
while contenido(notas, i) != None:
    print("El valor del indice",i,"es:",notas[i])
    suma += notas[i]
    i +=1

print("La media con el bucle while es:",suma/i)

# Mismo bucle con for
i = 0
suma = 0
for i in range(len(notas)):
   print("El valor del indice",i,"es:",notas[i])
   suma += notas[i]

print("La media es con el bucle for es:",suma/(i+1))

