x=int(input("Напишите год: "))

def is_year_leap(x):
    
    if x%4==0 and x%100!=0 or x%400==0:
        print("Год высокостный")
    else:
        print("Год не высокостный")

is_year_leap(x)

    
    