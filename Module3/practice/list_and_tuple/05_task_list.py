# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

k = 1
max_length = 0
for fruit in fruits:
    if len(fruit) > max_length:
        max_length = len(fruit)
for fruit in fruits:
    if len(fruit) < max_length:
        i = 0
        dif_length=max_length-len(fruit)
        while i < dif_length:
            fruit = " " + fruit
            i += 1
    print(str(k) + '.', fruit)
    k += 1

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
