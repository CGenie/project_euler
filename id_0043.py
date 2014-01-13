#!/usr/bin/python2
# #####################################################################
# id_0043.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import permutations

def gen_pandigitals_n_with_zero(n):
    digits = [str(x) for x in range(n + 1)]
    for c in permutations(digits):
        yield int(''.join(c))

def check_substring_divisibility(num):
    s = str(num)
    divs = [2, 3, 5, 7, 11, 13, 17]
    for x in range(1, 8):
        n = int(s[x:x + 3])
        if n % divs[x - 1] != 0:
            return False
    return True

if __name__ == '__main__':
    s = 0
    f = gen_pandigitals_n_with_zero(9)
    while True:
        try:
            ret = f.next()
            if check_substring_divisibility(ret):
                print "%d has substring divisibility property" % ret
                s += ret
        except StopIteration:
            break
    print s
