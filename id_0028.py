#!/usr/bin/python2
# #####################################################################
# id_0028.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def sum_of_spiral(n):
    # 1 in the center
    cnt = 1
    # the sum so far
    s = 1
    for side in range(1, (n - 1)/2 + 1):
        # the jump factor, at each side we have (2*k - 1) numbers
        jmp = 2*side
        # four vertices
        for x in range(4):
            cnt += jmp
            #print "Vertex at %d" % (cnt,)
            s += cnt
    return s

if __name__ == '__main__':
    print sum_of_spiral(1001)
