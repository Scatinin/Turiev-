#integer целые
#input ввести
#float дроби
print("Какую зарплату ты хочешь себе и другу?")
a=int(input())
b=int(input())
c=2
if a > b:
    print("Нечестно")
elif a < b:
    print("Видимо ты его очень уважаешь, ты мне нравишься")
elif (a * c) > b:
    print("Что то ты перебарщиваешь")
else:
    a = b
    print("Хороший выбор")

