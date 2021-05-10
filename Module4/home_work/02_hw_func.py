# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((y2 - y1) ** 2 + (x1 - x2) ** 2) ** 0.5
    pass


def shortest_line(p1, p2, p3):
    ab = distance(p1[0], p1[1], p2[0], p2[1])
    bc = distance(p2[0], p2[1], p3[0], p3[1])
    ac = distance(p1[0], p1[1], p3[0], p3[1])
    shortest = min(ab, bc, ac)
    if ab == shortest:
        return "AB"
    elif bc == shortest:
        return "BC"
    return "AC"



print("Самый короткий отрезок:",
      shortest_line((10, 12), (14, 18), (12, 12)))  # Выводим название отрезка, например “АС”.
