#!/usr/bin/python2
# #####################################################################
# id_0063.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def how_many_digits(num):
    return len(str(num))

if __name__ == '__main__':
    n = 0
    for i in range(1, 40):
        print i
        m = 1
        while True:
            r = how_many_digits(m**i)
            if r == i:
                n += 1
                print str(m) + "**" + str(i) + " = " + str(m**i)
            if r > i:
                break
            m += 1
    print n
