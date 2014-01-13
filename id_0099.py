#!/usr/bin/python
# #####################################################################
# id_0099.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import log

def greater((b, e), (B, E)):
    n1 = e*log(float(b))
    n2 = E*log(float(B))
    if n1 > n2:
        return 1
    else:
        return -1

if __name__ == '__main__':
    f = open('id_0099.txt')
    lst = []
    for line in f:
        pp = line.strip().split(',')
        lst.append(tuple(map(lambda x: int(x), pp)))
    M = 0
    BE = lst[0]
    for i, be in enumerate(lst):
        if greater(be, BE) == 1:
            M = i
            BE = be
    print M + 1
    print BE
