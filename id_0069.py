#!/usr/bin/python2
# #####################################################################
# id_0069.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0033 import gcd
from id_0003 import is_prime, prime_factors
from id_0008 import mul

def relatively_prime(n, m):
    return gcd(n, m) == 1

def totient(n):
    ret = 1
    for m in range(2, n):
        if relatively_prime(m, n):
            ret += 1
    return ret

d_totient = {1: 1}

def totient2(n):
    try:
        return d_totient[n]
    except KeyError:
        ret = n
        if is_prime(n):
            ret = n - 1
        else:
            fact = prime_factors(n)
            for p in fact:
               ret = ret*(p - 1)/p 
        k = 1
        while True:
            d_totient[n**k] = (n**(k - 1))*ret
            k += 1
            if n**k >= 10**6:
                break
        return d_totient[n]

if __name__ == '__main__':
    # read the wiki: http://en.wikipedia.org/wiki/Euler%27s_totient_function
    # in particular the chapter 'Growth of the function'
    lst_primes = [x for x in range(2, 50) if is_prime(x)]
    i = 0
    while True:
        n = mul(lst_primes[:i])
        if n > 10**6:
            n = mul(lst_primes[:(i - 1)])
            break
        i += 1
    print n
    
