#!/usr/bin/python2
# #####################################################################
# id_0042.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import sqrt

triangle = {}

def is_triangle_num(tn):
    try:
        return triangle[tn]
    except KeyError:
        s = 1 + 8*tn
        delta = int(sqrt(s))
        ret = (delta**2 - s == 0)
        triangle[tn] = ret
        return ret

def is_triangle_word(word):
    a = ord('a') - 1
    return is_triangle_num(sum([ord(x) - a for x in word.lower()]))

if __name__ == '__main__':
    f = open('./id_0042.txt')
    s = ""
    for line in f:
        s += line.strip()
    wrds = s.split(",")
    print wrds
    wrds = [x.strip("\"") for x in wrds]
    print wrds
    f.close()
    s = 0
    for x in wrds:
        if is_triangle_word(x):
            s += 1
    print s
