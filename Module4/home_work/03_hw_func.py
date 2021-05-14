# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def circle_in_circle(c1, c2, r1, r2):
    dist = distance(c1[0], c1[1], c2[0], c2[1])
    return dist < (r2 - r1) or dist < (r1 - r2)
    pass


def distance(x1, y1, x2, y2):
    return ((y2 - y1) ** 2 + (x1 - x2) ** 2) ** 0.5
    pass
