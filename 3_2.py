from math import *


def f(b, n, m):
    part1 = 0
    part2 = 1
    for i in range(1, b):
        part1 += (64 * (i ** 3 - (i ** 2 / 78)) ** 4 - i / 50 - exp(i) ** 5)
    cum = 0
    german = 1
    final = 0
    j = 1
    i = 1
    c = 1
    while j < m + 1:
        if i == b + 1:
            j += 1
            i = 1
            c = 1
            part2 *= final
            final = 0
            german = 1
        while i < b + 1:
            if c == n + 1:
                c = 1
                i += 1
                final += german
                german = 1
            while c < n + 1:
                cum = (45 * ((54 * i ** 3 - 7 - c / 56) ** 7) - j ** 3)
                german *= cum
                c += 1
    return part1 + part2


print(f(2, 3, 4))
