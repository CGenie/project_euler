#!/usr/bin/python2
# #####################################################################
# id_0018.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def read_triangle(s):
    return [[int(x) for x in y.strip().split(" ")] for y in s.split("\n")]

def find_maximal_path(arr):
    sums = []
    for i in range(len(arr) - 1, 1, -1):
        l = []
        for j in range(len(arr[i]) - 1):
            m = max(arr[i][j], arr[i][j + 1])
            l.append(m)
            arr[i - 1][j] += m
    arr[0][0] += max(arr[1][0], arr[1][1])
    print arr
    return arr[0][0]

if __name__ == '__main__':
    f = open("./id_0018.txt")
    l = []
    for line in f:
        l.append([int(x) for x in line.strip().split(" ")])
    print l
    print find_maximal_path(l)
