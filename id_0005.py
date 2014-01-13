#!/usr/bin/python2
# #####################################################################
# id_0005.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def evenly_divisible(n):
    s = n
    while True:
        d = True
        for x in range(2, n + 1):
            if s % x != 0:
                s += n
                d = False
                break
        if d:
            break
        else:
            d = True        
    return s

if __name__ == '__main__':
    print evenly_divisible(20)
