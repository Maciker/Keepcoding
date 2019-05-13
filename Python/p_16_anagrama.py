# Dos palabras son anagramas¿?
def isAnagram(p1, p2):
    lista1 = list(p1)
    lista1.sort()
    lista2 = list(p2)
    lista2.sort()

    return (lista1 == lista2)

print(isAnagram("casa","saca"))