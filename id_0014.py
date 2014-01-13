#!/usr/bin/python2
# #####################################################################
# id_0014.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def collatz_chain(n):
    s = 1
    r = n
    while True:
        r = collatz(r)
        s += 1
        if r == 1:
            break
    return s

def longest_chain(n):
    l = 0
    p = 0
    for x in range(1, n):
        c = collatz_chain(x)
        if x % 10000 == 0:
            print "x = " + str(x) + ", c = " + str(c)
        if l < c:
            l = c
            p = x
    return (l, p)

if __name__ == '__main__':
    print longest_chain(10**6)
