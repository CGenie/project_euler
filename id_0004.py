#!/usr/bin/python2
# #####################################################################
# id_0004.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def palindrome(n):
    """Find the largest palindrome made of n-digit numbers"""
    d = {}
    l = 0
    p = (0, 0)
    for i in range(10**n - 1, 10**(n - 1) - 1, -1):
        for j in range(i, 10**(n - 1) - 1, -1):
            s = str(i*j)
            if s == s[::-1]:
                d[(i, j)] = i*j
                if l < i*j:
                    l = i*j
                    p = (i, j)
    return d, l, p

if __name__ == '__main__':
    print palindrome(3)[1]
    print palindrome(3)[2]
