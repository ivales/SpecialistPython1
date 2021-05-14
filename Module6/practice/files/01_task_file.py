# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)
with open('data/limericks.txt', 'r', encoding="utf8") as f:
    count_lines=count_limer=0
    for line in f:
        print(line.rstrip())
        for ch in line.strip():
            if ch!=' ' or '\t':
                count_lines+=1
        if line.rstrip() == "":
            count_limer+=1
if count_limer!=0:
    count_limer+=1
print(count_lines)
print(count_limer)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего
