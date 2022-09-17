def late():
    while(True):
        print("Вы выбрали латэ")
        user_choose = input("Выберите добавку:")
        if user_choose == "1":
            print("Вы выбрали латэ с сахаром с вас 10$")
            user_choose = input("Введите сумму:")
            if user_choose == "10":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввелли не ту сумму!Нужно 10")
                break
        user_choose = input("Выберите добавку:")
        if user_choose == "2":
            print("Вы выбрали латэ с молоком с вас 11$")
            user_choose = input("Введите сумму:")
            if user_choose == "11":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввелли не ту сумму!Нужно 11")
                break
        user_choose = input("Выберите добавку:")
        if user_choose == "3":
            print("Вы выбрали латэ с лимоном с вас 12$")
            user_choose = input("Введите сумму:")
            if user_choose == "12":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввелли не ту сумму!Нужно 12")
                break
        else:
            break
def americano():
    while(True):
        print("Вы выбрали американо")
        user_choose = input("Выберите добавку:")
        if user_choose == "1":
            print("Вы выбрали американо с сахаром с вас 12$")
            user_choose = input("Введите сумму:")
            if user_choose == "12":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввелли не ту сумму!Нужно 12")
                break

        user_choose = input("Выберите добавку:")
        if user_choose == "2":
            print("Вы выбрали американо с молоком с вас 13$")
            user_choose = input("Введите сумму:")
            if user_choose == "13":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввелли не ту сумму!Нужно 13")
                break

        user_choose = input("Выберите добавку:")
        if user_choose == "3":
            print("Вы выбрали американо с лимоном с вас 14$")
            user_choose = input("Введите сумму:")
            if user_choose == "14":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввелли не ту сумму!Нужно 14")
        else:
            break
def zele():
    while(True):
        print("Вы выбрали зелье энергии")
        user_choose = input("Выберите добавку:")
        if user_choose == "1":
            print("Вы выбрали зелье с сахаром с вас 100$")
            user_choose = input("Введите сумму:")
            if user_choose == "100":
                print("Вот ваше зелье.Спасибо!")
                break
            else:
                print("Вы ввелли не ту сумму!Нужно 100")
                break

        user_choose = input("Выберите добавку:")
        if user_choose == "2":
            print("Вы выбрали зелье с молоком с вас 101$")
            user_choose = input("Введите сумму:")
            if user_choose == "101":
                print("Вот ваше зелье.Спасибо!")
                break
            else:
                print("Вы ввелли не ту сумму!Нужно 101")
                break

        user_choose = input("Выберите добавку:")
        if user_choose == "3":
            print("Вы выбрали зелье с лимоном с вас 102$")
            user_choose = input("Введите сумму:")
            if user_choose == "102":
                print("Вот ваше зелье.Спасибо!")
                break
            else:
                print("Вы ввелли не ту сумму!Нужно 102")
        else:
            break
        
while(True):
    print("ЦЕНЫ КОФЕ:\nЛатэ = 10\nАмерикано = 12\nЗелье = 100\nЦЕНЫ ДОБАВКИ:\nСахар = 0\nМолоко = 1\nЛимон = 2\nНОМЕРА КОФЕ:\nЛатэ = 1\nАмерикано = 2\nЗелье = 3\nНОМЕРА ДОБАВОК:\nСахар = 1\nМолоко = 2\nЛимон = 3")
    user_menu = input("Ваш выбор кофе:")
    if user_menu == "1":
        late()
    if user_menu == "2":
        americano()
    if user_menu == "3":
        zele()

        
