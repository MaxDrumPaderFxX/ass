from math import *

def f(z):
    if (z < 14):
        return z**4 + z**6 / 5 + 15 * ((z**3 / 10 - 2 - z**2))**7
    elif (z >= 14 and z < 91):
        return 65 * (67 * z**2)**4
    elif (z >= 91 and z < 164):
        return 12 * z + z**4 + 84 * (1 - 63 * z**2 - 50 * z**3)**7
    elif (z >= 164 and z < 209):
        return cos(z)**6 / 67 + (z - 0.02)**7 + ceil(z / 34 - z**2)**3
    else:
        return ceil(z)**5

print(f(206))