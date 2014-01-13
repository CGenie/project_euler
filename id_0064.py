#!/usr/bin/python2
# #####################################################################
# id_0064.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import sqrt
from id_0033 import gcd

def continued_fraction_sqrt(n):
    a = 1
    b = 0
    m = 1
    s = int(sqrt(n))
    while True:
        l = (a*s + b)/m
        yield l
        b = b - l*m
        aa = m*a
        bb = -m*b
        m = n*a*a - b*b
        a = aa
        b = bb
        am = gcd(a, m)
        bm = gcd(b, m)
        abm = gcd(am, bm)
        if abm > 1:
            a = a/abm
            b = b/abm
            m = m/abm
        if m == 0:
            raise StopIteration

if __name__ == '__main__':
    n = 2
    odd = 0
    period_len = 20
    limit = 13
    while True:
        f = continued_fraction_sqrt(n)
        r1 = f.next()
        lst = []
        cont_frac = True
        for i in range(period_len):
            try:
                lst.append(f.next())
            except StopIteration:
                cont_frac = False
                break
        # find a period
        if cont_frac:
            for l in range(1, period_len/2):
                first = lst[:l]
                next = []
                for x in range(period_len/l):
                    next.append(lst[x*l:(x + 1)*l])
                    has_period = True
                for x in next:
                    if first != x:
                        has_period = False
                        break
                if has_period:
                    print "sqrt(" + str(n) + ") = {" + str(r1) + "; " + str(lst[:l]) + "}, period of length " + str(l)
                    if l % 2 == 1:
                        print "n = " + str(n) + " -- odd period found"
                        odd += 1
                    break
            if not has_period:
                print "No period found..."
                raise Error
        if n >= limit:
            break
        n += 1
    print odd
        
