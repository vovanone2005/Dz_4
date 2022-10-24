from math import sqrt
a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))
c = int(input("Введите целое число c: "))
d  = b**2 - 4*a*c
if d > 0:
     x1 = (-b - math.sqrt(d))/ (2 * a)   
     x2 = (-b + math.sqrt(d)) / (2 * a)
elif d == 0:
     x = -b  / (2*a)
     print("x = %.2f" % x)
else:
     print("Корней нет")
