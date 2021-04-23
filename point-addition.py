import math
from fractions import Fraction as frac
a = 171
b = 853

# p = (0, 4)
# q = (4, 2)
O = (0, 0)
modulus = 2671

# slope = 0


def pointSum(p, q):
    slope = 0
    if p[0]==0 and p[1]==0:
        return q
    elif q[0]==0 and q[1]==0:
        return p
    else:
        if (p[0]==q[0] and p[1]==-q[1]):
            return (0,0)
        else:
            if p[0]==q[0] and p[1]==q[1]:
                slope = ((3*(p[0]**2)+a)/(2*(p[1]))) 
    
            else:
                if q[0]-p[0] == 0:
                    return (0,0)
                slope = ((q[1]-p[1])/(q[0]-p[0]))

   
    slope_fraction = (frac(slope).limit_denominator(10000)).as_integer_ratio()
    # print('SLOPE FRACTION: ', slope_fraction)
    slope = ((slope_fraction[0]) * (pow(slope_fraction[1], modulus-2, modulus))) % modulus

    # print('SLOPE: ', slope)

    x3 = ((slope**2) - p[0] - q[0]) % modulus
    y3 = (slope*(p[0]-x3)-p[1]) % modulus

    # print(x3, y3)
    return (x3, y3)
            
def doubleAndAdd(p, n):
    Q = (p[0],p[1])
    R = (0, 0)
    
    while n > 0:
        if n % 2 == 1:
            R = pointSum(R, Q)
        Q = pointSum(Q, Q)
        n = math.floor(n/2)
        # print('R: ', R)
    # print('R-final: ', R)
    return R



P = (2110, 543)
print("-----DoubleAndAdd-----")

point = doubleAndAdd(P, 1943)
print('Point: ', point)

# newP = (24, 14)
# times = 19

# i = 1
# ppp = (1432, 667)
# while i<=2761:
#     curPoint = doubleAndAdd(ppp, i)
#     print(i, curPoint)
#     if curPoint[0] == 2:
#         print(i)
#         break
#     i+=1


