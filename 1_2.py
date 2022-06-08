from math import *
def main(x,y):
    part1=(floor(0.02+y**2+x**3)**2)/(((71*y+59+39*y**3)**2)+cos(x)**4/50)
    part2=19*(acos(x**3-48*y**2-1)**3)
    part3=acos(x**2+53*y**3)
    return(part1+part2-part3)
print(main(0.85, 0.03))