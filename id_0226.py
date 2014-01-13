#!/usr/bin/python
# #####################################################################
# id_0226.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import sqrt, asin, pi

def S(x):
    n = int(x)
    return min(x - n, (n + 1) - x)

def circ(x):
    return 0.5 - sqrt(0.5*x - x**2)

def y(x):
    n = 50
    s = 0
    for j in range(n):
        s += S(2**j * x)/2**j
    return s

def roznica(x):
    return y(x) - circ(x)
    
def pkt_przeciecia():
    x_0 = 0.06
    x_1 = .08
    err = 1
    while err > 1E-10:
        x_m = .5*(x_0 + x_1)
        fm = roznica(x_m)
        #print(fm)
        if fm < 0:
            x_0 = x_m
        else:
            x_1 = x_m
        err = abs(fm)
    x_m = 0.5*(x_0 + x_1)
    return x_m

def I(x):
    err = 1E-15
    if abs(x) < err:
        return 0.
    if abs(x - 1) < err:
        return 0.5
    if x >= 1:
        return 0.5 + I(x - 1)
    if x > 0.5 and x < 1:
        return 0.5 - I(1 - x)
    if x >= 0 and x <= 0.5:
        return 0.25*I(2*x) + 0.5*x**2
    if x < 0:
        return -I(-x)

if __name__ == '__main__':
    # wyznacz punkty przeciecia
    x_0 = pkt_przeciecia()
    print("x_0 = ", x_0)
    # drugi latwo policzyc:
    x_1 = 0.5
    # teraz liczymy \int_{x_0}^{x_1} s
    i0 = I(x_0)
    i1 = I(x_1)
    print("i0 = ", i0, ", i1 = ", i1)
    # pole pod wykresem kola:
    pp = 0.5*(0.5 - x_0) + ((4*x_0 - 1)*sqrt(1 - (4*x_0 - 1)**2) - pi / 2 - asin(1 - 4*x_0))/32
    print("pp = ", pp)
    print("ans = ", i1 - i0 - pp)
