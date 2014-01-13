#!/usr/bin/python2
# #####################################################################
# id_0056.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

if __name__ == '__main__':
    m = 0
    for a in xrange(100):
        for b in xrange(100):
            c = a**b
            ss = str(c)
            s = sum([int(x) for x in ss])
            if m < s:
                print "New maximal sum of digits found for a = %d and b = %d" % (a, b)
                m = s
    print m
