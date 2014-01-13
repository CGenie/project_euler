#!/usr/bin/python2
# #####################################################################
# id_0013.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def first_n_digits(num, n):
    s = str(num)
    return s[:n]

if __name__ == '__main__':
    f = open("./id_0013.txt")
    s = 0
    for line in f:
        s += int(line.strip())
    print first_n_digits(s, 10)
