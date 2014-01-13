#!/usr/bin/python2
# #####################################################################
# id_0070.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime
from id_0008 import mul
from id_0062 import is_permutation
from id_0069 import totient2

if __name__ == '__main__':
    # read the wiki: http://en.wikipedia.org/wiki/Euler%27s_totient_function
    lst_primes = [x for x in range(2, 4000) if is_prime(x)]
    #lst_primes.reverse()
    ratio = 50.0
    print lst_primes
    i = 1
    for p in range(len(lst_primes)):
        for q in range(p + 1, len(lst_primes)):
            s = lst_primes[p]*lst_primes[q]
            t = (lst_primes[p] - 1)*(lst_primes[q] - 1)
            ss = "s = %d, t = %d" % (s, t)
            if s < 10**7 and is_permutation(t, s):
                ss += " -- a permutation"
                r = float(s)/float(t)
                if ratio > r:
                    ss += " -- new minimum found"
                    ratio = r
                    print ss
        
