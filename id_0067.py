#!/usr/bin/python2
# #####################################################################
# id_0067.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0018 import find_maximal_path

if __name__ == '__main__':
    f = open("./id_0067.txt")
    l = []
    for line in f:
        l.append([int(x) for x in line.strip().split(" ")])
    print l
    print find_maximal_path(l)
