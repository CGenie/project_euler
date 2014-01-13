#!/usr/bin/python2
# #####################################################################
# id_0038.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def is_pandigital(num):
    s = str(num)
    l = len(s)
    digits = [str(x) for x in range(1, 10)]
    if l != 9:
        return False
    for x in s:
        try:
            digits.remove(x)
        except ValueError:
            return False
    return True

def pandigital_concatenated_product(num):
    s = str(num)
    x = 2
    while len(s) < 9:
        s += str(x*num)
        x += 1
    return (is_pandigital(int(s)), x - 1, int(s))

if __name__ == '__main__':
    m = 0
    M = 0
    for x in xrange(1, 10**5):
        ret = pandigital_concatenated_product(x)
        if ret[0] and ret[1] > 1:
            print "%d is concatenated pandigital with n = %d" % (x, ret[1])
            if ret[2] > M:
                m = x
                M = ret[2]
    print M
