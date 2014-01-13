#!/usr/bin/python2
# #####################################################################
# id_0074.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def digits(n):
    return [int(x) for x in str(n)]

d_fact = {0 : 1}
for n in xrange(1, 11):
    d_fact[n] = n*d_fact[n - 1]

def sum_fact(lst):
    return sum([d_fact[n] for n in lst])

def num_from_digits(lst):
    return int(''.join([str(x) for x in lst]))

def factorions(n):
    d = {}
    for x in xrange(11):
        d[x] = d_fact[x]
    for x in xrange(10, n):
        lst = digits(x)
        try:
            d[x] = d_fact[lst[-1]] + d[num_from_digits(lst[:-1])]
        except KeyError:
            d[x] = sum_fact(lst)

    return d

if __name__ == '__main__':
    t = factorions(10**7)
    print num_from_digits([1, 2, 3, 4])
    print sum(t.keys())
