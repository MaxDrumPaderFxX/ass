from math import *


def f(z, y):
    n = len(z)
    z.insert(0, 0)
    y.insert(0, 0)
    part1 = 0
    for i in range(1, n + 1):
        part1 += (atan(51 - z[n + 1 - i] - 34 * y[n + 1 - ceil(i / 4)] ** 3)) ** 6
    return 57 * part1


print(f([-0.31, 0.94, -0.51, -0.77, -0.44, 0.87],
        [-0.35, -0.06, -0.84, 0.07, -0.51, 0.91]))
