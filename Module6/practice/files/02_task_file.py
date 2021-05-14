# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
with open('data/sold.txt', 'r', encoding="utf-8") as f:
    str_prices = ''
    for line in f:
        str_prices += line
str_prices = str_prices.replace('\n', ' ')
str_prices = str_prices.split()
prices=[]
for price in str_prices:
    prices.append(float(price))
print(sum(prices))
print(max(prices))
print(min(prices))
