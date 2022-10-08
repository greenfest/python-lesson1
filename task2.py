import math
print("Введите координаты точки А через запятую:")
a = input().replace(" ", "").split(",")
print("Введите координаты точки B через запятую:")
b = input().replace(" ", "").split(",")
length = math.sqrt((int(b[0]) - int(a[0]))**2 + (int(b[1]) - int(a[1]))**2)
print("Расстояние между точками А и В = {:0.2f}".format(length))