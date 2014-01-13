#!/usr/bin/python2
# #####################################################################
# id_0053.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def comb_num(n, k):
    ret = 1
    for x in range(n - k):
        ret = ret*(n - x)/(x + 1)
    return ret

if __name__ == '__main__':
    ret = 0
    for n in range(1, 101):
        r = 0
        while True:
            if r > n/2:
                break
            c = comb_num(n, r)
            if c > 10**6:
                ret += (n + 1) - 2*r
                break
            r += 1
        if n % 10 == 0:
            print "n = %d" % n
    print "A total of %d combinations is greater than a million" % ret
