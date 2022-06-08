from math import *

def f(b, n, m):
    part_1 = 0
    for i in range(1, b + 1):
        part_1 += (64 * (i**3 - i**2 / 78)**4 - i / 50 - exp(i)**5)

    part_2 = 1
    for j in range(1, m + 1):
        pt_1 = 0
        for i in range(1, b + 1):
            pt_2 = 1
            for c in range(1, n + 1):
                pt_2 *= (45 * (54 * i**3 - 7 - c / 56)**7 - j**3)
            pt_1 += pt_2
        part_2 *= pt_1

    return part_1 + part_2

print(f(6, 2, 4))