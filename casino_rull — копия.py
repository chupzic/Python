import random

cash = 0

red = [2,4,6,8,10,14,16,18,20,22,24,26,28,30,32,34,36]

black = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]

white = [12]

user_money = input("Ваш депозит: ")
user_bid = input("Сколько ставите: ")
user_money = int(user_money)
user_bid = int(user_bid)

user_choose = input("(Выберите 0-красное, 1-чёрное или 2-белое)На что ставите: ")
user_choose = int(user_choose)

rand_color = random.randint(1, 36)

rand_number = random.randint(0, 2)

if rand_number in (red):
    print('Выпало красное')

if rand_number in (black):
    print('Выпало черное')

if rand_number in(white):
    print('Выпало белое')

def proverka():
    while True :
        try :
            assert user_money >= user_bid, 'Ставка не может быть больше текущего баланса'

        except ValueError :
            print('Ставка не может быть больше текущего баланса')
        break
proverka()



def game() :
        global peremen
        peremen = user_money - user_bid
        peremen_w = user_money + user_bid
        global cash
        cash = user_bid

        if rand_number == user_choose :
            cash += user_bid * 2
            peremen = cash + user_bid
            cash = int(cash)
            print(f"Победа! Ваш депозит:", peremen_w)
            if rand_number in (red):
                print('Выпало красное')
            if rand_number in (black):
                print('Выпало черное')
            if rand_number in(white):
                print('Выпало белое')
        else :
            cash -= user_bid / 2
            cash = int(cash)
            print(f"Проигрыш! Ваш депозит:", peremen)



def enter():
    while True:
        cont = int (input("Введите если 1 если да, 2 если нет. Хотите продолжить?:"))
        if cont  == 1:
            proverka()
            game()
        else:
            break

proverka()
game()
enter()