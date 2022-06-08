def f(n):
    if (n == 0):
        return 0.56
    elif (n == 1):
        return 0.21
    else:
        return (f(n - 1)**2 / 28 - f(n - 1) / 66 - f(n - 2)**3)

print(f(8))