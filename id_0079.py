#!/usr/bin/python3.1
# #####################################################################
# id_0079.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

if __name__ == '__main__':
    # eliminate duplicates
    d = {}
    f = open('id_0079.txt')
    for l in f:
        i = int(l)
        d[i] = 1
    for x in d.keys():
        print(x)
    # and solve by hand! ;)
