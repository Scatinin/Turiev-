a=int(input("Введите 5-х число: "))
if a>9999 and a<100000:
    a1= a // 10000
    a2= a % 10000
    a3= a2 // 1000
    a4= a2 % 1000
    a5= a4 // 100
    a6= a4 % 100
    a7= a6 //10
    a8= a6 %10
    print ( a7, a8)
else:
    print ("Неверное")
