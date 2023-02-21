a=int(input("Введите 3-х число: "))
if a>99 and a<1000:
    a1= a // 100
    a2= a % 100
    a3= a2 // 10
    a4= a3*10
    a5= a2 % 10
    a6= a5*100
    c= a6+a4+a1
    d= c-a
    print (a1, a2, a3, a4, a5, a6 )
    print (c )
    print (d )
    
else:
    print ("Неверное число")