#!/usr/bin/python
# #####################################################################
# id_0243.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import sys
import time

from helper_py3 import memoize
#from id_0069 import totient2


@memoize()
def gcd(a, b):
    if b == 1:
        return 1
    c = a//b
    r = a - c*b
    if r == 0:
        return b
    return gcd(b, r)
        

@memoize()
def R(n):
    # 1 is resilient
    s = 1
    for x in range(2, n):
        if gcd(n, x) == 1:
            s += 1
    return s


# coprime pair generation
# this is slow...
coprimes = {}
def branch(mn):
    m, n = mn
    return [(2*m - n, m), (2*m + n, m), (m + 2*n, n)]


class FastTotient(object):
    def __init__(self, n):
        self.totients = [1]*n  # [1 for i in range(n)]
        print "array generated"
        for i in range(2, n):
            if self.totients[i] == 1:
                for j in range(i, n, i):
                    self.totients[j] *= (i - 1)
                    k = j / i
                    while k % i == 0:
                        self.totients[j] *= i
                        k /= i

    def __call__(self, i):
        return self.totients[i]


if __name__ == '__main__':
    n = 5
    numerator = 15499
    denominator = 94744
    M = float(15499)/94744
    print "M = " + str(M)
    start = time.time()
    p = 9
    totient = FastTotient(10**p)
    print totient(11)
    print totient(12)
    print totient(13)
    print 'took %r' % (time.time() - start)
    print 'Testing totients one by one'
    while True:
        r = totient(n)
#        if n % 100 == 0:
#            print "n = " + str(n) + ", R(n) = " + str(r)
        if r*denominator < (n - 1)*numerator:
            print "sol: " + str(n)
            break
        n += 1

    sys.exit()

    # coprime numbers generation -- very slow and unstable
    # (how to sort these???)
    lst = [(2, 1), (3, 1)]
#    for n in range(14):
#        print('generation %d' % n)
#        new_lst = []
#        for elem in lst:
#            if elem[0] in coprimes:
#                coprimes[elem[0]] += 1
#            else:
#                coprimes[elem[0]] = 1
#
#            new_lst.extend(branch(elem))
#
#        lst = new_lst
#
#    # compute the ratios
#    mm = None
#    nn = None
#    for k, v in coprimes.items():
#        if v*denominator < (k - 1)*numerator:
#            if mm is None or k < mm:
#                mm = k
#                nn = v
#
#    print(mm, nn)
#    print(coprimes[180])
#    print(R(180))
