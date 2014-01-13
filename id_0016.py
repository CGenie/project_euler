#!/usr/bin/python2
# #####################################################################
# id_0016.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def sum_digits(n):
    s = str(n)
    return sum([int(x) for x in s])

if __name__ == '__main__':
    print sum_digits(2**1000)
