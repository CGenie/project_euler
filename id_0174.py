#!/usr/bin/python
# #####################################################################
# id_074.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def comb(k, M):
    return M//(4*(k + 1)) - 1 - k

if __name__ == '__main__':
    M = 10**6
    t = []
    L = {}
    n = 1
    while n < M:
        print("n = ", n)
        k = 0
        while True:
            s = (k + 1)*4
            for i in range(k + 1):
                s += 4*(n + 2*i)
            if s > M:
                break
            t.append(s)
            k += 1
        n += 1
    print(t)
