# 12 Задача
r=int(input("Введите радиус круга : ")) #s1 площадь круга
a=int(input("Введите сторону квадрата: ")) #s2 площадь квадрата
p=3.14
s1=p*r**2
s2=a**2
if s1 > s2:
    print("Площадь круга больше")
else:
    print("площадь квадрата больше")

