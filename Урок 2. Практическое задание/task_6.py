"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random


def guess_num(n=-1, a=random.randint(0, 100), i=10):
    if n != a and i > 0:
        n = int(input('Введите число: '))
        i -= 1
        if n > a:
            print(f'Загаданное число меньше, осталось {i} попыток')
        elif n < a:
            print(f'Загаданное число больше, осталось {i} попыток')
        return guess_num(n, a, i)
    elif n == a:
        return 'Вы угадали!'
    else:
        return f'Ваши попытки исчерпаны. Загаданное число: {a}'


print(guess_num())
