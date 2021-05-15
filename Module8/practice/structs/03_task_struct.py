# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random


def gen_lst():
    n = 100
    lst = []
    for i in range(0, n - 1):
        lst.append(random.randint(-100, 100))
    return lst


def counts_less_10(lst):
    lst2 = []
    for l in lst:
        if lst.count(l) <= 10:
            lst2.append(l)
    return len(lst2)


def pos_sum(lst):
    lst2 = []
    for l in lst:
        if l > 0:
            lst2.append(l)
    return sum(lst2)


def sr_ar(lst):
    lst2 = []
    for l in lst:
        if l % 2 == 0:
            lst2.append(l)
    return float(sum(lst2)) / len(lst)


lst=gen_lst()
print(lst)
print(pos_sum(lst))
print(sr_ar(lst))
