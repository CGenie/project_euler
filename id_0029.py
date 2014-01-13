#!/usr/bin/python2
# #####################################################################
# id_0029.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def ab_combinations(A, B):
    d = {}
    for a in range(2, A + 1):
        for b in range(2, B + 1):
            d[a**b] = 1
    return len(d)

if __name__ == '__main__':
    print ab_combinations(100, 100)
