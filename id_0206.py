#!/usr/bin/python
# #####################################################################
# id_0206.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import sqrt

d_endings = {}

def fill_endings():
    for x in range(10):
        d_endings[x] = (x*x) % 10

def get_digits_from_ending(ending):
    ret = []
    for x in range(10):
        if d_endings[x] == ending:
            ret.append(x)
    return ret

num = [1, 10, 2, 10, 3, 10, 4, 10, 5, 10, 6, 10, 7, 10, 8, 10, 9, 10, 0]

if __name__ == '__main__':
    fill_endings()
    numlen = len(num)
    start = int(sqrt(6*10**11))
    end = int(sqrt(7*10**11) + 1)
    print(d_endings)
    print(start, end)
    Blist = []
    for B in range(start, end):
        B2 = B**2
        goodB = True
        for i in range(3):
            if (B2 % 10**(2*i + 1))//(10**(2*i)) != (10 - i) % 10:
                goodB = False
                break
        if goodB:
            print("possible sol B = ", B)
            Blist.append(B)
    n = 0
    n2 = 0
    for A in range(10**4, 10**5):
        for B in Blist:
            n = 10**5*A + B
            n2 = n**2
            goodn = True
            for i in range(10):
                if (n2 % 10**(2*i + 1))//(10**(2*i)) != (10 - i) % 10:
                    goodn = False
                    break
            if goodn:
                print("sol = ", n)
                break
        if A % 10000 == 0:
            print("A = ", A)
        
