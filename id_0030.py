#!/usr/bin/python2
# #####################################################################
# id_0030.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def is_sum_of_nth_powers(num, n):
    return num == sum([int(x)**n for x in str(num)])

if __name__ == '__main__':
    s = 0
    # this maximum is enough, but overall, it cannot be greater than 6*9**5 = 354294
    for n in range(2, 200000):
        if is_sum_of_nth_powers(n, 5):
            print "n = %d is sum of 5th powers of it's digits" % n
            s += n
    print s
