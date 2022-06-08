def f(y, z):
    res = 0
    n = len(y)
    y.insert(0, 0)
    z.insert(0, 0)
    for i in range(1, n + 1):
        res += 34 * (y[n + 1 - i]**3 + 1 + 34 * z[n + 1 - i]**2)**3
    return 45 * res

print(f([0.77, -0.17, 0.67], [0.58, 0.69, 0.22]))