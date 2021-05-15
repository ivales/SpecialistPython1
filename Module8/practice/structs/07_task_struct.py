# Доработайте предыдущую программу так, чтобы каждый сгенерированный сотрудник
# был уникальным(не должны повторяться комбинации Имя + Фамилия).
# Доработайте предыдущую программу так, чтобы каждый сгенерированный сотрудник
# был уникальным(не должны повторяться комбинации Имя + Фамилия).
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


big_dict = {}
for i in range(1000):
    list=[]
    list.append(random_list())
    big_dict[list[0][0] + ' ' + list[0][1]] = str(list[0][2]) + ' ' + list[0][3] + ' ' + str(list[0][4])
print(big_dict)
