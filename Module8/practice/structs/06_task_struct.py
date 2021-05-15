# Вы написали программу для работы с сотрудниками и вам ее необходимо протестировать.
# Для теста нужны большие списки сотрудников (100+).
# Вбивать вручную столько данных займет очень много времени.
# Напишите программу, генерирующую списки сотрудников со следующими параметрами:
# 1. Имя
# 2. Фамилия
# 3. Возраст
# 4. Профессия
# 5. Зарплата
# Примечание: Данные сгенерированных сотрудников могут повторяться
import random
import string


def generate_random_string():
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(20))
    return rand_string


def random_list():
    list_employee = [generate_random_string(), generate_random_string(), random.randint(18, 100),
                     generate_random_string(), random.randint(20000, 100000)]
    return list_employee


big_list=[]
for i in range(1000):
    big_list.append(random_list())
