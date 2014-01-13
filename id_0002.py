#!/usr/bin/python2
# #####################################################################
# id_0002.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

d = {}

def fib(n):
    try:
        return d[n]
    except KeyError:
        if n == 0:
            d[n] = 1
        elif n == 1:
            d[n] = 1
        else:
            d[n] = fib(n - 1) + fib(n - 2)
        return d[n]

def fib_iter():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

if __name__ == '__main__':
    s = 0
    while True:
        if fib(s) > 4E6:
            break
        s += 1
    print s
    ret = 0
    for x in range(s):
        v = fib(x)
        if v % 2 == 0:
            ret += v
    print ret
