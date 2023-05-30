x=int(input("Напишите номер месяца: "))

def season(x):
    if 1<=x<=12:
        if 1<=x<=2 and 12:
            print("Этот месяц ЗИМЫ")
        elif 3<=x<=5:
            print("Этот месяц ВЕСНЫ")
        elif 6<=x<=8:
            print("Этот месяц ЛЕТА")
        elif 9<=x<=11:
            print("Этот месяц ОСЕНИ")
        else:
            print("Неправильная запись")
    else:
        print("Не верный месяц")
    
season(x)