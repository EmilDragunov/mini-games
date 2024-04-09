import random


def is_valid(n, x, y):  # Проверка на соответствие введенного значения условию.
    return n.isdigit() and float(n) - int(float(n)) == 0 and x <= int(n) <= y


def format_total(total):  # Формат количества попыток.
    if total == 1 or total == 21 or total == 31 or total == 41 or total == 51:
        return f'{total} попытку'
    elif 2 <= total % 10 <= 4:
        return f'{total} попытки'
    elif 5 <= total <= 20 or 25 <= total <= 30 or 35 <= total <= 40:
        return f'{total} попыток'


def input_num(down_num=0, up_num=999999999999999999):  # Ввод данных.
    while True:
        guess = input()
        if is_valid(guess, down_num, up_num):
            return int(guess)
        else:
            print(f'А может быть все-таки введем целое число от {down_num}'
                  f'до {up_num}?')


def compare_num(down_num, up_num):  # Сравнение значений.
    num = random.randint(down_num, up_num)
    total = 0
    while True:
        n = input_num(down_num, up_num)
        total += 1
        if n < num:
            print('Не угадали, попробуйте число побольше')
        elif n > num:
            print('Мимо, назовите число поменьше')
        else:
            print(f'Победа!!! Вы угадали ответ за {format_total(total)},'
                  'поздравляем!')
            break


def continue_game():  # Предложение продолжить игру.
    ans = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Вроде, взрослый человек, '
                        'а на простой вопрос ответить не может...\n'
                        'Продолжим ("д"/"н")?\n')
        elif ans in ('n', 'н'):
            print('До новых встреч!!!')
            return False
        else:
            return True


def game():  # Запуск игры.
    print('Добро пожаловать в числовую угадайку!')
    while True:
        print('Укажите, в каком диапазоне Вы готовы угадывать числа:\n')
        x, y = input_num(), input_num()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y, '\n')
        compare_num(x, y)
        if continue_game():
            continue
        else:
            break


game()  # Вызов игры.
