#!/usr/bin/python
# #####################################################################
# id_0097.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def int2bin(n):
    s = []
    while n > 0:
        s.append(n % 2)
        n = (n >> 1)
    return s

d_2 = [1]

def power_of_2_last_10_digits(n):
    L = 10**10
    try:
        return d_2[n]
    except IndexError:
        d_2.append(2*power_of_2_last_10_digits(n - 1) % L)
        return d_2[n]

if __name__ == '__main__':
    m = 28433
    p = 7830457
    l = int2bin(m)
    L = 10**10
    s = 1
    print "Computing last 10 digits of powers of 2..."
    for x in range(1, p, 700):
        r = power_of_2_last_10_digits(x)
        print x
    print "Computing the last 10 digits of the number..."
    for i, x in enumerate(l):
        pp = power_of_2_last_10_digits(i + p)
        if x == 1:
            s = (s + pp) % L
    print "ans = " + str(s)
    
