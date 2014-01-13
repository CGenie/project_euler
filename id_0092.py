#!/usr/bin/python
# #####################################################################
# id_0092.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
M = 10**7

d_ssd = {'1' : 1}

def sum_squares_of_digits(n):
    l = list(str(n))
    l.sort()
    s = ''.join(l)
    try:
        return d_ssd[s]
    except KeyError:
        d_ssd[s] = sum([int(x)**2 for x in s])
        return d_ssd[s]

d = {1 : 1}

def gennum(n):
    try:
        return d[n]
    except KeyError:
        gn = sum_squares_of_digits(n)
        if gn == 89:
            d[n] = 89
        elif gn == 1:
            d[n] = 1
        else:
            d[n] = gennum(sum_squares_of_digits(n))
        # do all the stuff for n*10, n*100, etc:
        p = n*10
        while p < M:
            d[p] = d[n]
            p *= 10
        return d[n]

if __name__ == '__main__':
    s = 0
    for n in range(1, M):
        r = 0
        try:
            r = d[n]
        except KeyError:
            r = gennum(n)
        if r == 89:
            s += 1
            if s % 10000 == 0:
                print(n)
    print("ans = ", s)
