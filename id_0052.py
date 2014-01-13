#!/usr/bin/python2
# #####################################################################
# id_0052.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import log

if __name__ == '__main__':
    # only numbers starting with 10**, 11**, 12**, 13**, and 14**
    # should be considered
    s = 10
    while True:
        if s % 1000 == 0:
            print "s = %d" % s
        ss = str(s)
        if int(ss[0]) > 1 or int(ss[1]) > 4:
            l = int(log(s, 10)) + 1
            s = 10**l
        sn = [list(str(x*s)) for x in range(2, 7)]
        goodnum = True
        for d in ss:
            try:
                for n in range(5):
                    sn[n].remove(d)
            except ValueError:
                goodnum = False
                break
        if goodnum:
            print "s = %d is a hit" % s
            break
        s += 1
