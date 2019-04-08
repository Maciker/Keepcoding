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
# No meter datos en el codigo a capon, mejor en variables
value01 = 31
value02= 28
value03 = 30

"""if month == 1:
    days = day
elif month == 2:
    days = value01 + day
elif month == 3:
    days = value01 + value02 + day
elif month ==4:
    days = value01 + value02 + value01 + day
elif month == 5:
    days = value01 + value02 + value01 + value03 + day
elif month == 6:
    days = value01 + value02 + value01 + value03 + value01 + day
elif month == 7:
    days = value01 + value02 + value01 + value03 + value01 + value03 + day
elif month == 8:
    days = value01 + value02 + value01 + value03 + value01 + value03 + value01 + day
elif month == 9:
    days = value01 + value02 + value01 + value03 + value01 + value03 + value01 + value01 + day
elif month == 10:
    days = value01 + value02 + value01 + value03 + value01 + value03 + value01 + value01 + value03 + day
elif month == 11:
    days = value01 + value02 + value01 + value03 + value01 + value03 + value01 + value01 + value03 + value01 + day
else:
    days = value01 + value02 + value01 + value03 + value01 + value03 + value01 + value01 + value03 + value01 + value03 + day"""
# Usamos Acumulador para tener menos repeticiones
days = day
if month > 1:
    days = value01 + days
if month > 2:
    days = value02 + days
if month > 3:
    days = value03 + days
if month > 4:
    days = value01 + days
if month > 5:
    days = value03 + days
if month > 6:
    days = value01 + days
if month > 7:
    days = value03 + days
if month > 8:
    days = value01 + days
if month > 9:
    days = value01 + days
if month > 10:
    days = value03 + days
if month > 11:
    days = value01 + days

prob = (days / 365) * 100
birth=(year-age)

print(name,"naciste en",birth,"con una probabilidad del", prob)
print("o en", birth - 1,"con una probabilidad del", 100-prob)