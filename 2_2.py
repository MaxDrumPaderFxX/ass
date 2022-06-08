from math import *
def f(y):
    if y<-23:
        return tan(y)**2/13 - y**5 - (6*y**3)**7/21
    elif (y>=-23) and (y<5):
        return (29*y**3)**7/54 - 69 - 45*(1+56*y)
    elif (y>=5) and (y<39):
        return 24*(ceil(y)**6) -45*(y**3 +y/66)**7-y**2
    else:
        return y**2+(12+y**3+y**2)**6 + 98*y-y**2-3*y**3
print(f(-17))