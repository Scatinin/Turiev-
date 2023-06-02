a=input("Размер денежного вклада. руб:")
years=input("На какой срок: ")


def bank(a,years):              
    try:
        a=int(a)
        years=int(years)
        x=a*1.1**years
        print(x)
        
    except ValueError:
        print("Ошибка")
bank(a,years)
    
