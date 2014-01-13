#!/usr/bin/python3.1
# #####################################################################
# id_0082.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import product

def diag_pos(diag, pos, M, N):
    return (M - diag + pos - 1, N - pos - 1)

def diag_pos2(diag, pos, M, N):
    return (M - diag - pos - 1, pos)

def solve(filename):
    d = []
    f = open(filename)
    for l in f:
        s = l.strip().split(',')
        d.append([int(x) for x in s])
    #print(d)
    N = len(d)
    M = len(d[0])
    f = product(range(M), range(N))
    ds = {}
    for (x, y) in f:
        ds[(x, y)] = 0
    for y in range(N):
        ds[(y, N - 1)] = d[y][N - 1]
    # going from right column to the left
    for x in range(M - 2, -1, -1):
        # going from top to bottom
        for y in range(N):
            # first possibility: go right
            s = ds[(y, x + 1)]
            # second possibility: go up
            # remember that we can go up many times
            #if y > 0:
            #    s = min(s, d[y - 1][x] + ds[(y - 1), (x + 1)])
            for k in range(y):
                ss = sum([d[y - w - 1][x] for w in range(k + 1)])
                s = min(s, ss + ds[(y - k - 1), (x + 1)])
            # third possibility: go down
            # again, we can go down many times
            #if y < N - 1:
            #    s = min(s, d[y + 1][x] + ds[(y + 1), (x + 1)])
            for k in range(N - 1 - y):
                ss = sum([d[y + w + 1][x] for w in range(k + 1)])
                s = min(s, ss + ds[(y + k + 1), (x + 1)])
            ds[(y, x)] = s + d[y][x]
            #print("x = ", x, ", y = ", y, ", ds = ", ds[(y, x)])
    #print(ds)
    #for y in [ds[(y, 0)] for y in range(N)]:
    #    print(y)
    s = min([ds[(y, 0)] for y in range(N)])
    return s

if __name__ == '__main__':
    print("sol = ", solve('id_0082.txt'))
