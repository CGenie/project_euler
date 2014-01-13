#!/usr/bin/python
# #####################################################################
# id_0120.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def rem(a, n):
    return ((-1)**n + 1 + n*a*(-1)**(n - 1) + n*a) % (a**2)

def rmax(a):
    m = 0
    for k in range(1, 2*a):
        m = max(m, rem(a, k))
    return m

if __name__ == '__main__':
    s = 0
    for k in range(3, 1001):
        ret = rmax(k)
        print("k = " + str(k) + ", rmax(k) = " + str(ret))
        s += ret
    print("sol = " + str(s))
