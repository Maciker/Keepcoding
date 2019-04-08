# Uno de los prieros programas del curso, muchas repeticiones, fallos, etc
name = input("¿Como te llamas? " )
strage = input("Hola, "+name+" ¿Cuantos años tienes? ")
stryear = input(name+" ¿En que año estamos? ")
strmonth = input(name+" ¿En que mes estamos? ")
strday = input(name+ "¿Que dia es? ")
#happy = input(name+" ¿Has cumplido años ya?")
age = int(strage)
year = int(stryear)
month = int(strmonth)
day = int(strday)

"""if happy == 'S':
    birth=(year-age)
else:
    birth=(year-age)-1
print(name+" naciste en el año ",birth)"""

if month == 1:
    days = day
elif month == 2:
    days = 31 + day
elif month == 3:
    days = 31 + 28 + day
elif month ==4:
    days = 31 + 28 + 31 + day
elif month == 5:
    days = 31 + 28 + 31 + 30 + day
elif month == 6:
    days = 31 + 28 + 31 + 30 + 31 + day
elif month == 7:
    days = 31 + 28 + 31 + 30 + 31 + 30 + day
elif month == 8:
    days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + day
elif month == 9:
    days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + day
elif month == 10:
    days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
elif month == 11:
    days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
else:
    days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day

prob = (days / 365) * 100
birth=(year-age)

print(name,"naciste en",birth,"con una probabilidad del", prob)
print("o en", birth - 1,"con una probabilidad del", 100-prob)