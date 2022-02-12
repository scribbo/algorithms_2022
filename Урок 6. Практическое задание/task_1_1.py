"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""
from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper

# Подсчитать четные и нечетные цифры введенного натурального числа.


def count_even_odd(n, even=0, odd=0):
    if n != 0:
        if (n % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_even_odd((n // 10), even, odd)
    print(f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})')


@memory
def func_call(n):
    count_even_odd(n)


n = int(input('Введите число: '))
func_call(n)


@memory
def func_2():
    num = input('Введите число: ')
    even = 0
    odd = 0
    for el in num:
        if int(el) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'В числе {num} {even} четных цифр и {odd} нечетных')


func_2()

# снижение размера памяти произошло в результате использования цикла вместо рекурсии (большое число)

#рекурсия
#Введите число: 904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456
#Количество четных и нечетных цифр в числе равно: (130, 140)
#Выполнение заняло 0.3125 Mib

#цикл
#Введите число: 904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456
#В числе 904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456904560934756097304967039456 130 четных цифр и 140 нечетных
#Выполнение заняло 0.01953125 Mib


# однако на малых числах снижения размера памяти не наблюдается

#рекурсия
#Введите число: 90456093475609730
#Количество четных и нечетных цифр в числе равно: (8, 9)
#Выполнение заняло 0.0078125 Mib

#цикл
#Введите число: 90456093475609730
#В числе 90456093475609730 8 четных цифр и 9 нечетных
#Выполнение заняло 0.01953125 Mib