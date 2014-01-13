#!/usr/bin/python2
# #####################################################################
# id_0009.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def is_pythagorean(a, b, c):
    return (c**2 - a**2 - b**2) == 0

for i in range(1000):
    for j in range(i, 1000):
        k = 1000 - i - j
        lst = [i, j, k]
        lst.sort()
        if is_pythagorean(*lst):
                print lst
                print lst[0]*lst[1]*lst[2]
