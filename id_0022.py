#!/usr/bin/python2
# #####################################################################
# id_0022.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def name_alphabetical_value(name):
    d = {}
    a = ord('A')
    return sum([ord(x) - a + 1 for x in name])

if __name__ == '__main__':
    f = open("./id_0022.txt")
    s = ""
    for line in f:
        s += line.strip()

    names = s.split(",")
    names = [x.strip("\"") for x in names]
    names.sort()
    s = 0
    for i, name in enumerate(names):
        s += (i + 1)*name_alphabetical_value(name)
    print s
