#!/usr/bin/python2
# #####################################################################
# id_0101.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from numpy.linalg import solve

def coeff(n, f):
    x = range(1, n + 1)
    y = map(f, x)
    mtx = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(x[i]**j))
        mtx.append(row)
    sol = solve(mtx, y)
    return lambda x: int(round(sum(map(lambda i: sol[i]*(x**i), range(n)))))

def fit(f_interp, f_original):
    n = 1
    while True:
        if f_interp(n) != f_original(n):
            return f_interp(n)
        n += 1

if __name__ == '__main__':
    f_orig = lambda x: sum(map(lambda i: (-1)**i * x**i, range(11)))
    s = 0
    for x in range(1, 11):
        r = fit(coeff(x, f_orig), f_orig)
        s += r
        print r
    print "sol = " + str(s)
