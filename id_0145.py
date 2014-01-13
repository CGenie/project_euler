#!/usr/bin/python
# #####################################################################
# id_0145.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

# rozwiazanie analityczne
@memoize()
def cnt(n):
    if n == 2:
        return 20
    if n == 3:
        return 100
    if n == 5:
        return 0
    if n == 7:
        return 50000
    return cnt(2)*cnt_0(n - 2)
    
def cnt_0(n):
    s = 0
    if n == 2:
        for x in range(10):
            for y in range(10):
                if x + y < 10 and (x + y)%2 == 1:
                    s += 1
        return s
    if n == 3:
        return 100
    return cnt_0(2)*cnt_0(n - 2)

if __name__ == '__main__':
    s = 0
    for n in range(2, 9):
        print("n = ", n, ", #(n) = ", cnt(n))
        s += cnt(n)
    print("sol = ", s)
    print(cnt_0(4), cnt_0(2))
    s = 0
    for x in range(10):
        for y in range(10):
            if x + y < 10 and (x + y)%2 == 0:
                s += 1
    print(s)
