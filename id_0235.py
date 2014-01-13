#!/usr/bin/python
# #####################################################################
# id_0235.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from decimal import *

getcontext().prec = 20

def s(r, n):
    return (900 - 903*r)*(1 - r**n)/(1 - r)**2 + 3*(1 - (n + 1)*r**n)/(r - 1) + 6*10**11

def ser(r, n):
    s = Decimal.from_float(0.0)
    for k in range(1, n + 1):
        s += (900 - 3*k)*r**(k - 1)
    return s

if __name__ == '__main__':
    # secant method
    l = Decimal.from_float(1.001)
    r = Decimal.from_float(1.01)
    a = s(l, 5000)
    b = s(r, 5000)
    while True:
        m = (l + r)/2
        ret = s(m, 5000)
        if ret > 0:
            a = ret
            l = m
        if ret < 0:
            b = ret
            r = m
        print("(a, l) = (" + str(a) + ", " + str(l) + "),  (b, r) = (" +  str(b) + ", " + str(r) + ")")
        if r - l < Decimal.from_float(10**(-15)):
            print("ser(m, n) = " + str(ser(m, 5000) + 6*10**11))
