#!/usr/bin/python2
# #####################################################################
# id_0050.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime

lst_primes = []
for n in xrange(2, 10**3):
    if is_prime(n):
        lst_primes.append(n)

def sum_consecutive_primes(num):
    i = 0
    while True:
        k = 0
        sum_of_primes = False
        tst = num
        while True:
            tst -= lst_primes[i + k]
            if tst == 0:
                return (k + 1)
            if tst < 0:
                break
            k += 1
        if lst_primes[i] > num:
            break
        i += 1
    return 0

if __name__ == '__main__':
    for n in xrange(10**3, 10**6):
        if is_prime(n):
            lst_primes.append(n)
    print "lst completed"

    m = 0
    for i in range(len(lst_primes) - 1, 0, -1):
        x = lst_primes[i]
        ret = sum_consecutive_primes(x)
        if m < ret:
            m = ret
            print "For %d we have %d primes" % (x, ret)
        if i % 10 == 0:
            M = sum(lst_primes[:m])
            print "x = %d, i = %d and the minimal possible sum for primes is %d" % (x, i, M)
            if M > x:
                break
        
