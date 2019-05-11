# Mejorando el programa 0_01
name = input("¿Como te llamas? " )
strage = input("Hola, "+name+" ¿Cuantos años tienes? ")
stryear = input(name+" ¿En que año estamos? ")
strmonth = input(name+" ¿En que mes estamos? ")
strday = input(name+ "¿Que dia es? ")
# Inputs los pasamos a int
age = int(strage)
year = int(stryear)
month = int(strmonth)
day = int(strday)
# Ahora usaremos un array
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Usamos Acumulador para tener menos repeticiones
days = day
index = 0
while index < month -1:
    days += months[index]
    index += 1

prob = (days / 365) * 100
birth=(year-age)

print(name,"naciste en",birth,"con una probabilidad del", prob)
print("o en", birth - 1,"con una probabilidad del", 100-prob)