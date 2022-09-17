little_cup_price = 5
big_cup_price = 10

coffee_list = [
                ["Americano+", 10],
                ["Latte", 15],

              ]

summ = 0

def CheckBill():
    global summ
    while True:
        print(f"Your summ is {summ}")
        try:
            user_pay = int(input("Input your money: "))
        except ValueError:
            print("Error! Input only number")
        else:
            if user_pay > 0 and user_pay <= 5000:
                if user_pay > summ:
                    print(f"Your summ is {user_pay}, need summ is {summ}. Your difference is {user_pay-summ}")
                    print("Have a nice day!")
                    break
                elif user_pay == summ:
                    print("Have a nice day!")
                    break
                else:                    
                    print(f"Your summ is {user_pay}, need summ is {summ}. You need add {summ-user_pay} money.")
                    summ -= user_pay
            else:
                print("Bad money!")

def ChooseVolume(coffee_name, price):
    global summ
    while True:
        print(f"{coffee_name}\n1.Little\n2.Big\n3.Return")
        user_choose = input("Choose menu item: ")
        if user_choose == "1":
            summ = price+little_cup_price            
            break
        elif user_choose == "2":
            summ = price+big_cup_price
            break
        elif user_choose == "3":
            break
        else:
            print("Error. Bad menu item!")

def ChooseAmericano():
    ChooseVolume(coffee_list[0][0], coffee_list[0][1])
    CheckBill()

def ChooseLatte():
    ChooseVolume(coffee_list[1][0], coffee_list[1][1])
    CheckBill()

while True:
    print(f"Coffee\n1.{coffee_list[0][0]}\n2.{coffee_list[1][0]}\n3.Exit")
    user_choose = input("Choose menu item: ")
    if user_choose == "1":
        ChooseAmericano()
    elif user_choose == "2":
        ChooseLatte()
    elif user_choose == "3":
        break
    else:
        print("Error. Bad menu item!")
