a=int(input("Введите 4-х значное число: "))
if 10000>a>999:
    a1= a // 1000
    a2= a % 1000
    a3= a2 // 100
    a4= a2 % 100
    a5= a4 // 10
    a6= a4% 10
    a7= a1+a3+a5+a6
    a8= a1*a3*a5*a6
    print (a1, a2, a3, a4, a5, a6)
    print (a7)
    print (a8)
else:
    print ("Неверное число")

