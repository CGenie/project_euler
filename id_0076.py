#!/usr/bin/python3.1
# #####################################################################
# id_0076.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import itertools

def sums(N):
    w = 0
    for L in range(1, N):
        #print("L = ", L)
        lst = []
        dct = {}
        for x in range(L):
            lst.append(range(1, N - x))
        f = itertools.product(*lst)
        for d in f:
            ss = sum(d)
            dd = N - ss
            if dd > 0:
                ll = list(d) + [dd]
                ll.sort()
                dct[tuple(ll)] = 1
        w += len(dct.keys())
    return w

ns = {}
def new_sums(N, L):
    try:
        return ns[(N, L)]
    except KeyError:
        if N == L:
            ns[(N, L)] = 1
        elif L == 2:
            ns[(N, L)] = int(N/2)
        else:
            s = N - 1
            ss = 0
            while s > 0:
                ss += new_sums(s, L - 1)
                s -= L
            ns[(N, L)] = ss
        return ns[(N, L)]

def Sums(N):
    s = 0
    for L in range(2, N + 1):
        s += new_sums(N, L)
    return s

if __name__ == '__main__':
    N = 100
    
    print("w = ", Sums(N))
