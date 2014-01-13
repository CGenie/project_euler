#!/usr/bin/python
# #####################################################################
# id_0162.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

@memoize()
def N(k):
    if k == 3:
        return 4
    return (15 + 16*(k - 1))*N(k - 1)
    
if __name__ == '__main__':
    s = N(3)
    for k in range(4, 17):
        s = N(k)
    print(str(hex(s)))
