#!/usr/bin/python
# #####################################################################
# id_0125.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

def gen_square_sums(ll):
    # generate sums of consecutive squares of length ll
    n = 1
    while True:
        slic = range(n, n + ll)
        yield sum([x**2 for x in slic])
        n += 1

#@memoize()
def is_palindromic(ss):
    if len(ss) <= 1:
        return True
    return ss[0] == ss[-1] and is_palindromic(ss[1:-1])

if __name__ == '__main__':
    d = {}
    ll = 2
    M = 10**8
    s = 0
    while True:
        gss = gen_square_sums(ll)
        n = next(gss)
        if n >= M:
            # no more sums can be generated
            break
        # iterate over sums
        while n < M:
            if is_palindromic(str(n)):
                print("n = ", n, " is palindromic, ll = ", ll)
                # some numbers repeat...
                d[n] = 1
                #s += n
            n = next(gss)
        ll += 1
    s = sum(d.keys())
    print("sol = ", s)
