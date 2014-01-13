#!/usr/bin/python
# #####################################################################
# id_0173.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def comb(k, M):
    return M//(4*(k + 1)) - 1 - k

if __name__ == '__main__':
    M = 10**6
    k = 0
    s = 0
    while True:
        r = comb(k, M)
        #print(r)
        if r > 0:
            s += r
        else:
            break
        k += 1
    print("sol = ", s)
