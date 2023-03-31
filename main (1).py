hours = float(input("Введите количество отработанных часов: "))
credit = float(input("Введите остаток по кредиту: "))
food_money = float(input("Введите количество денег на еду: "))

salary = (200 * hours / 2 ** 3) + hours

if salary >= credit + food_money:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придется работать")