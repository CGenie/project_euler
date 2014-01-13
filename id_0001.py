#!/usr/bin/python2
# #####################################################################
# id_0001.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

# the following is WRONG, it calculates number k*3*5 TWICE
def ss(m):
    s = 0
    s += sum([x for x in range(0, m, 3)])
    s += sum([x for x in range(0, m, 5)])
    return s

# this is correct
def ss2(m):
    l = []
    for x in range(m):
        if x % 3 == 0:
            l.append(x)
        elif x % 5 == 0:
            l.append(x)
    return sum(l)

if __name__ == '__main__':
    print ss2(1000)
