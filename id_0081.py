#!/usr/bin/python3.1
# #####################################################################
# id_0081.py
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
    M = len(d)
    N = len(d[0])
    f = product(range(M), range(N))
    ds = {}
    for (x, y) in f:
        ds[(x, y)] = 0
    ds[(M - 1, N - 1)] = d[M - 1][N - 1]
    # bottom triangle + main diagonal
    for diag in range(1, M):
        #print("diag = ", diag)
        for pos in range(diag + 1):
            #print("pos = ", pos)
            s = 10**10
            # check if bottom
            (x, y) = diag_pos(diag, pos, M, N)
            if y < N - 1:
                s = min(s, ds[(x, y + 1)])
            # check if right
            if x < M - 1:
                s = min(s, ds[(x + 1, y)])
            ds[(x, y)] = d[x][y] + s
    # top triangle without main diagonal
    for diag in range(1, M):
        #print("diag = ", diag)
        for pos in range(M - diag):
            #print("pos = ", pos)
            s = 10**10
            # check if bottom
            (x, y) = diag_pos2(diag, pos, M, N)
            if y < N - 1:
                s = min(s, ds[(x, y + 1)])
            # check if right
            if x < M - 1:
                s = min(s, ds[(x + 1, y)])
            ds[(x, y)] = d[x][y] + s
    return ds[(0, 0)]

if __name__ == '__main__':
    print("sol = ", solve('id_0081.txt'))
