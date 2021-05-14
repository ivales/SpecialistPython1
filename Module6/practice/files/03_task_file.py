# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день
items_dict = {}
with open('data/items_sold.txt', 'r', encoding='utf-8') as f:
    for line in f:
        item_list = line.split()
        for item in item_list:
            pair = item.split(':')
            if items_dict.get(pair[0]) is not None:
                items_dict[pair[0]] += float(pair[1])
            else:
                items_dict[pair[0]] = float(pair[1])
print(items_dict)
print(sum(items_dict.values()))
max_item = list(items_dict.values())[0]
max_item_type=list(items_dict.keys())[0]
for key,value in items_dict.items():
    print(f'{key} : {value:.2f}')
    if value > max_item:
        max_item=value
        max_item_type=key
print(max_item_type)
