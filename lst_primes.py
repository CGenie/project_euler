#!/usr/bin/python2
# #####################################################################
# lst_primes.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime as ip
from math import sqrt
import pickle

Max = 10**6

lst_primes = [2]
for n in xrange(3, Max, 2):
    ul = int(sqrt(n)) + 1
    for x in lst_primes:
        is_prime = True
        if x > ul:
            break
        if n % x == 0:
            is_prime = False
            break
    if is_prime:
        print "%d is prime" % n
        lst_primes.append(n)

# print "Asserting equality..."
# for n in xrange(2, Max):
#     assert((n in lst_primes) == ip(n))
#     if n % 1000 == 0:
#         print "n = %d" % n
# print "done"

f = open("./primes.pickle", 'wb')
pickle.dump(lst_primes, f)
f.close()
