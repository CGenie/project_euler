#!/usr/bin/python
# #####################################################################
# id_0091.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import product

dsq = {(1, 1) : 3}

def sqr(a, b):
    try:
        return dsq[(a, b)]
    except KeyError:
        if b > 1:
            s = 0
            if (2*a >= b):
                s = (b - 1 % 2)
            z = 1 if (a >= 2*b) else 0
            p = max(0, b - a)
            print((a, b), p)
            dsq[(a, b)] = 3*a + s + z + sqr(a, b - 1) + p
        else:
            s = 0
            if (2*b >= a):
                s = (a - 1 % 2)
            z = 1 if (b >= 2*a) else 0
            p = max(0, a - b)
            print((a, b), p)
            dsq[(a, b)] = 3*b + s + z + sqr(a - 1, b) + p
    return dsq[(a, b)]

dchk = {}

def check_triangle(pta, ptb):
    try:
        return dchk[(pta, ptb)]
    except KeyError:
        p1 = pta[0]**2 + pta[1]**2
        p2 = ptb[0]**2 + ptb[1]**2
        p3 = (pta[0] - ptb[0])**2 + (pta[1] - ptb[1])**2
        lst = [p1, p2, p3]
        lst.sort()
        dchk[(pta, ptb)] = ((lst[0] > 0) and (lst[2] == lst[0] + lst[1]))
    return dchk[(pta, ptb)]

dsqn = {(1, 1): 3}

def sqr_naive(a, b):
    try:
        return dsqn[(a, b)]
    except KeyError:
        if b > 1:
            s = 0
            # select a point from the top boundary
            for x_top in range(a + 1):
                pta = (x_top, b)
                # select another point
                # first one from the top
                for x_other in range(x_top, a + 1):
                    if check_triangle(pta, (x_other, b)):
                        s += 1
                # now from below the top
                for x_other, y_other in product(range(a + 1), range(b)):
                    if check_triangle(pta, (x_other, y_other)):
                        s += 1
            # if x_top == 0 then we can safely add a triangles
            #s += a
            dsqn[(a, b)] = s + sqr_naive(a, b - 1)
        else:
            s = 0
            for y_right in range(b + 1):
                pta = (a, y_right)
                for y_other in range(y_right, b + 1):
                    if check_triangle(pta, (a, y_other)):
                        s += 1
                for x_other, y_other in product(range(a), range(b + 1)):
                    if check_triangle(pta, (x_other, y_other)):
                        s += 1
            #s += b
            dsqn[(a, b)] = s + sqr_naive(a - 1, b)
        return dsqn[(a, b)]

if __name__ == '__main__':
    #print(sqr(2, 4))
    #print(sqr(15, 50))
    #print(sqr(50, 50))
    print(sqr_naive(2, 2))
    print(sqr_naive(10, 10))
    print(sqr_naive(20, 20))
    print(sqr_naive(30, 30))
    print(sqr_naive(30, 50))
    print(sqr_naive(40, 50))
    print(sqr_naive(50, 50))
    
