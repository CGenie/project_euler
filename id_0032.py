#!/usr/bin/python2
# #####################################################################
# id_0032.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from copy import deepcopy
from itertools import combinations, permutations

def is_pandigital(n):
    digits = range(1, 10)
    n_digits = [int(x) for x in str(n)]
    for d in n_digits:
        try:
            digits.remove(d)
        except ValueError:
            # digit repeated, not pandigital
            return False
    # now try to make products of the left-over digits
    dd = deepcopy(digits)
    for k in range(1, len(dd)):
        for cc in combinations(dd, k):
            for c in permutations(cc):
                digits = deepcopy(dd)
                pandig = True
                a = sum([d*10**i for i, d in enumerate(c)])
                if n % a == 0 and n/a > 0:
                    for d in c:
                        try:
                            digits.remove(d)
                        except ValueError:
                            # digit repeated, not pandigital
                            pandig = False
                            break
                    b = [int(x) for x in str(n/a)]
                    for d in b:
                        try:
                            #print "Removing %d from b" % d
                            digits.remove(d)
                        except ValueError:
                            # a digit doesn't exist, break
                            pandig = False
                            break
                    if pandig and len(digits) == 0:
                        print "n = %d is pandigital with a = %d, b = %d" % (n, a, n/a)
                        return True
    return False

# this is better
def generate_pandigitals():
    digits = range(1, 10)
    for k in range(1, 5):
        for AA in combinations(digits, k):
            leftover = range(1, 10)
            for x in AA:
                leftover.remove(x)
            for A in permutations(AA):
                a = sum([d*10**i for i, d in enumerate(A)])
                #print "a = %d" % a
                for j in range(4 - k, 6 - k):
                    for BB in combinations(leftover, j):
                        leftoveragain = deepcopy(leftover)
                        for x in BB:
                            leftoveragain.remove(x)
                        for B in permutations(BB):
                            leftoveragainagain = deepcopy(leftoveragain)
                            pandig = True
                            b = sum([d*10**i for i, d in enumerate(B)])
                            c = [int(x) for x in str(a*b)]
                            if len(leftoveragain) < len(c):
                                pandig = False
                            else:
                                for x in c:
                                    try:
                                        leftoveragainagain.remove(x)
                                    except ValueError:
                                        # not possible
                                        pandig = False
                            if pandig and leftoveragainagain == []:
                                yield (a, b)

if __name__ == '__main__':
    s = 0
    d = {}
    f = generate_pandigitals()
    while True:
        try:
            r = f.next()
            d[r[0]*r[1]] = 1
            print "r = %d = %d * %d is pandigital" % (r[0]*r[1], r[0], r[1])
        except StopIteration:
            break
    print sum(d.keys())
