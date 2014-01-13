#!/usr/bin/python2
# #####################################################################
# id_0040.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def generate_digits():
    n = 0
    while True:
        for x in str(n):
            yield int(x)
        n += 1

if __name__ == '__main__':
    f = generate_digits()
    pwr = 0
    dmul = 1
    f.next()
    for x in xrange(1, 10**6 + 1):
        d = f.next()
        if x % 10**pwr == 0:
            pwr += 1
            dmul *= d
            print "x = %d, digit = %d" % (x, d)
    print dmul
