#!/usr/bin/python2
# #####################################################################
# id_0055.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0036 import is_palindrome

def is_Lychrel_below_1000(num):
    n = 0
    while True:
        ss = list(str(num))
        ss.reverse()
        rev = int(''.join(ss))
        num = num + rev
        if is_palindrome(str(num)):
            return False
        if n == 50:
            return True
        n += 1

if __name__ == '__main__':
    cnt = 0
    for n in xrange(1, 10000):
        if is_Lychrel_below_1000(n):
            cnt += 1
            print "%d is Lychrel" % n
    print cnt
