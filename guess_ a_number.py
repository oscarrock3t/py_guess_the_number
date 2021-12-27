import random


def get_num():
    temp = input()
    if not temp.isdigit():
        print('Это не число!')
        return 'err'
    else:
        return int(temp)


def check_win(q, answer, t):
    if q == answer:
        print('***Вы угадали, поздравляем!***')
        print(f'Это заняло у Вас {t} попыток')
        return True
    elif q > answer:
        print('Cлишком МАЛО, попробуйте еще раз')
    elif q < answer:
        print('Слишком МНОГО, попробуйте еще раз')
    return False


def start():
    if input() in ('y', 'yes', 'да', 'Да', 'д', 'Yes', 'Y'):
        play()
    else:
        print('Пока')


def play():
    rand = random.randint(1, 100)
    tries = 0
    print('Загадано число от 1 до 100. Попробуйте угадать!')
    while True:
        print('Введите число:', end=' ')
        input_digit = get_num()
        if input_digit == 'err':
            continue
        tries += 1
        if check_win(rand, input_digit, tries):
            break
    print('Хотите сыграть ещё раз?', end=' ')
    start()


print('Начать игру?')
start()
