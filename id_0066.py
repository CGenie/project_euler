#!/usr/bin/python2
# #####################################################################
# id_0066.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import sqrt
from id_0003 import is_prime
from id_0064 import continued_fraction_sqrt
from id_0065 import generate_fraction

d_sqrt = {}

def is_square(num):
    try:
        n = d_sqrt[num]
    except KeyError:
        d_sqrt[num] = int(sqrt(num))
        n = d_sqrt[num]
    return n*n == num

# def solves_equation(x, y, D):
#     if (x*x - 1) % D != 0:
#         return False
#     yy = (x*x - 1)/D
#     if not is_square((x*x - 1)/D) or yy != y*y:
#         return False
#     return True

def solves_equation(x, y, D):
    return x*x - 1 == D*y*y

if __name__ == '__main__':
    limit = 1000
    D = 1
    lst_D = []
    while True:
        if not is_square(D):
            lst_D.append(D)
        if D >= limit:
            break
        D += 1
    m = 0
    for D in lst_D:
        f = continued_fraction_sqrt(D)
        lst = []
        while True:
            r = f.next()
            lst.append(r)
            fr = generate_fraction(lst)
            if solves_equation(fr.numerator, fr.denominator, D):
                if fr.numerator > m:
                    m = fr.numerator
                    print "D = %d, x = %d, y = %d, m = %d" % (D, fr.numerator, fr.denominator, m)
                break
    print m
