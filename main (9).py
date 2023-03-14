#Задание 13
x = int(input("Значение x: "))
a = int(input("Катет прил.: "))
b = int(input("Катет против.: "))
c = int(input("Гипотенуза: "))
if x <= 3.14/4:
    cos = a/c
    q1=cos*x
    print(q1)
else:
    sin = b/c
    q2=sin*x
    print(q2)


































#       /|
#c     / |
#     /  |
#    /   |
#   /    |       a(прил)
#  /     |
# /      |
#/       
#---------
#     b(против)








