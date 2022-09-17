bol = 10
mid = 15
small = 20

#def late_raz():
 #   while (True):
  #          print ("Вы выбрали латэ")
   #         user_raz = input("Большая чашка = 1\nСредняя чашка = 2\nМаленькая чашка = 3\nВыберите свою:")
    #        if user_raz == "1":
     #           print ("Вы выбрали большую чашку")
      #          dob_late()
       #     elif user_raz == "2":
        #        print ("Вы выюрали среднюю чашку")
         #       dob_late()
          #  elif user_raz == "3":
           #     print ("Вы выбрали маленькую чашку")
            #    dob late
def late():
    while (True):
            user_choose = input ("Выберите добавку:")
            if user_choose == "1":
                print("Вы выбрали латэ с сахаром\nС вас 10$")
                user_choose = input("Введите сумму:")
                if user_choose == "10":
                    print ("Вот ваш кофе.Спасибо!")
                    break
                else:
                    print ("Вы ввели не ту сумму!Нужно 10")
                    break
            elif user_choose == "2":
                print ("Вы выбрали латэ с молоком\nС вас 12$")
                user_choose = input("Введите сумму:")
                if user_choose == "12":
                    print ("Вот ваш кофе.Спасибо!")
                    break
                else:
                    print ("Вы ввели не ту сумму")
                    break
            elif user_choose == "3":
                print("Вы выбрали латэ с лимоном\nС вас 13$")
                user_choose = input("Введите сумму:")
                if user_choose == "13":
                    print("Вот ваш кофе.Спасибо!")
                    break
                else:
                    print("Вы ввели не ту сумму")
                    break
            else:
                break
def americano():
    while (True):
        print("Вы выбрали американо")
        user_choose = input("Выберите добавку:")
        if user_choose == "1":
            print("Вы выбрали американо с сахаром\nС вас 15$")
            user_choose = input("Введите сумму:")
            if user_choose == "15":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввели не ту сумму!Нужно 10")
                break
        elif user_choose == "2":
            print("Вы выбрали американо с молоком\nС вас 17$")
            user_choose = input("Введите сумму:")
            if user_choose == "17":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввели не ту сумму")
                break
        elif user_choose == "3":
                print("Вы выбрали американо с лимоном\nС вас 18$")
                user_choose = input("Введите сумму:")
                if user_choose == "18":
                    print("Вот ваш кофе.Спасибо!")
                    break
                else:
                    print("Вы ввели не ту сумму")
                    break
        else:
            break
def esspresso():
    while (True):
        print("Вы выбрали экспрессо")
        user_choose = input("Выберите добавку:")
        if user_choose == "1":
            print("Вы выбрали эксрперсо с сахаром\nС вас 10$")
            user_choose = input("Введите сумму:")
            if user_choose == "10":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввели не ту сумму!Нужно 10")
                break
        elif user_choose == "2":
            print("Вы выбрали эксрессо с молоком\nС вас 12$")
            user_choose = input("Введите сумму:")
            if user_choose == "12":
                print("Вот ваш кофе.Спасибо!")
                break
            else:
                print("Вы ввели не ту сумму")
                break
        elif user_choose == "3":
                print("Вы выбрали экспрессо с лимоном\nС вас 13$")
                user_choose = input("Введите сумму:")
                if user_choose == "13":
                    print("Вот ваш кофе.Спасибо!")
                    break
                else:
                    print("Вы ввели не ту сумму")
                    break
        else:
            break

while (True):
    print ("МЕНЮ ЦЕН НА КОФЕ:\nЛатэ = 10$\nАмерикано = 15$\nЭкспрессо = 10$\nЦЕНЫ НА ДОБАВКИ:\nСахар = 0$\nМолоко = 2$\nЛимон = 3$\nЦЕНЫ ЧАШЕК:\nБольая = 15\nСредняя = 10\nМаленькая = 5\nНОМЕРА КОФЕ:\nЛатэ = 1\nАмерикано = 2\nЭкспрессо = 3\nНОМЕРА ДОБАВОК:\nСахар = 1\nМолоко = 2\nЛимон = 3")

    user_menu = input("Выберите кофе:")
    if user_menu == "1":
        late()

    elif user_menu == "2":
        americano()

    elif user_menu == "3":
        esspresso()
    else:
        pass
    
