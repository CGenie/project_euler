#!/usr/bin/python3.1
# #####################################################################
# id_0085.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
d = {(1, 1): 1}

def rect(a, b):
    try:
        return d[(a, b)]
    except KeyError:
        if b > 1:
            d[(a, b)] = rect(a, b - 1) + b*int(a*(a + 1)/2)
        elif a > 1:
            d[(a, b)] = rect(a - 1, b) + a*int(b*(b + 1)/2)
        return d[(a, b)]

if __name__ == '__main__':
    M = 2*10**6
    err = 10**6
    A = 1
    B = 1
    for a in range(1, 2000):
        for b in range(1, 2000):
            r = rect(a, b)
            if abs(r - M) < err:
                err = abs(r - M)
                A = a
                B = b
                print("A = ", A, ", B = ", B, ", err = ", err)
            
