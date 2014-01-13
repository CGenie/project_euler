#!/usr/bin/python2
# #####################################################################
# id_0037.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime

def is_truncatable_prime(num):
    s = str(num)
    l = len(s)
    if not is_prime(num):
        return False
    for x in range(1, l):
        lft = s[:x]
        rgt = s[x:]
        if not is_prime(int(lft)) or not is_prime(int(rgt)):
            return False
    return True

if __name__ == '__main__':
    cnt = 0
    s = 0
    n = 11
    while cnt < 11:
        if is_truncatable_prime(n):
            s += n
            cnt += 1
            print "%d is truncatable" % n
        n += 1
    print s
