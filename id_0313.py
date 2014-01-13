#!/usr/bin/python
# #####################################################################
# id_0313.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

@memoize()
def nummoves(m, n):
    return (m + n - 3)*4 + 1

if __name__ == '__main__':
    print(nummoves(4, 5))
