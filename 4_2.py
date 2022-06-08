def f(x):
    if x==0:
        return 0.13
    if x==1:
        return 0.07
    if x>=2:
        return (3*f(x-1)**3 +1 +17*f(x-2))/24
print(f(8))