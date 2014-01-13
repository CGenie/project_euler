#!/usr/bin/python2
# #####################################################################
# id_0072.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def npf(dmax):
    N = dmax + 1;
    totient = range(N)
    for n in xrange(2, N):
        if totient[n] == n:
            for k in xrange(n, N, n):
                totient[k] *= (n - 1)
                totient[k] //= n
    return sum(totient[2:])

if __name__ == '__main__':
    print npf(10**6)
