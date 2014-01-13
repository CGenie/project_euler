#!/usr/bin/python
# #####################################################################
# id_0095.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

@memoize()
def factors(n):
    ret = [1]
    for x in range(2, n//2 + 1):
        if n % x == 0:
            ret.append(x)
    return ret

@memoize()
def d(n):
    return sum(factors(n))

def make_chain(start):
    lst = [start]
    while True:
        x = d(lst[-1])
        if x in lst:
            break
        if x > 10**6:
            lst = []
            break
        lst.append(x)
    if lst:
        return lst[lst.index(x):]
    return []
        

if __name__ == '__main__':
    m = 0
    n = 1
    saved_n = 0
    print(min(make_chain(5916)))
    while True:
        ret = make_chain(n)
        if ret:
            l = len(ret)
            if l > m:
               saved_n = n
               m = l
               print("saved_n = ", saved_n, ", m = ", m)
        n += 1
        if n == 10**6:
            break
        if n % 1000 == 0:
            print("n = ", n, ", saved_n = ", saved_n, ", m = ", m)
    print("sol = ", saved_n)
