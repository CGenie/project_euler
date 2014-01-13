#!/usr/bin/python2
# #####################################################################
# id_0047.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime
from math import sqrt
from helper import unique

prime_factors = {}

def find_prime_factors(num):
    try:
        return prime_factors[num]
    except KeyError:
        ret = []
        if is_prime(num):
            ret = [num]
        else:
            for n in xrange(2, num/2 + 1):
                if is_prime(n) and (num % n) == 0:
                    ret.append(n)
        prime_factors[num] = ret
        return ret

distinct_factors = {}

def count_distinct_factors(num):
    try:
        return distinct_factors[num]
    except KeyError:
        c = 0
        if is_prime(num):
            c = 1
        else:
            p = 2
            while num != 1:
                if num % p == 0:
                    c += 1
                    while num % p == 0:
                        num /= p
                p += 1
            distinct_factors[num] = c
        return c

def has_k_consecutive_distinct_prime_factors(n, k):
    l = 0
    for l in range(k):
        lst = find_prime_factors(n + l)
        if len(lst) < k:
            return False
    return True

def find_k_consecutive_distinct_prime_factors(k):
    n = 2
    while True:
        if n % 1000 == 0:
            print "n = %d" % n
        ret = has_k_consecutive_distinct_prime_factors(n, k)
        if ret:
            return n
        n += 1

if __name__ == '__main__':
    print find_k_consecutive_distinct_prime_factors(4)
    # n = 2
    # cnt = 0
    # while True:
    #     if n % 1000 == 0:
    #         print n
    #     if count_distinct_factors(n) == 4:
    #         cnt += 1
    #     else:
    #         cnt = 0
    #     if cnt == 3:
    #         print (n - 3)
    #         break
    #     n += 1
