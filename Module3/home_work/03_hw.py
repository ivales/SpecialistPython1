# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random

n = 10
numbers = []
for i in range(0, n):
    numbers.append(random.randint(-100, 100))
summa = 0
for el in numbers:
    if el > 0 and el % 2 == 0:
        summa += el
print(summa)
# TODO: your code here
