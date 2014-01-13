#!/usr/bin/python
# #####################################################################
# id_0205.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from random import randint
from itertools import product

d_pp = {}
d_cc = {}

def piramid_peter_intro():
    for n in range(9, 37):
        d_pp[n] = 0
    lst = range(1, 5)
    prd = product(lst, lst, lst, lst, lst, lst, lst, lst, lst)
    for p in prd:
        s = sum(p)
        d_pp[s] += 1

def cubic_collin_intro():
    for n in range(6, 37):
        d_cc[n] = 0
    lst = range(1, 7)
    prd = product(lst, lst, lst, lst, lst, lst)
    for p in prd:
        s = sum(p)
        d_cc[s] += 1

if __name__ == '__main__':
    piramid_peter_intro()
    cubic_collin_intro()
    n = 4**9 * 6**6
    s = 0
    for a in range(9, 37):
        p_a = d_pp[a]
        for b in range(6, a):
            s += p_a * d_cc[b]
    print("s = ", s, ", n = ", n, "s/n = ", float(s)/n)

    s = 0
    n = 10**7
    for x in range(n):
        s1 = sum([randint(1, 4) for j in range(9)])
        s2 = sum([randint(1, 6) for q in range(6)])
        if x % 10000 == 1:
            print("s = ", s, "x = ", x, "s/x = ", float(s)/x)
        if s1 > s2:
            s += 1
    print("s = ", s, "n = ", n, "s/n = ", float(s)/n)

