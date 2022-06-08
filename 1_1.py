from math import *
def main(z, x):
    part_1 = sqrt(60 * pow(tan(68 * z**2 + 5 * x + 58), 7))
    part_2 = 42 * pow(abs(z), 4)
    part_3 = pow(22 * x - 1 - x**2, 5)
    return part_1 + part_2 + part_3

print(main(-0.28, 0.7))