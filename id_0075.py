#!/usr/bin/python3.1
# #####################################################################
# id_0075.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

if __name__ == '__main__':
    d = {}
    #for x in range(750000):
    #    d[x] = {}
    m = 1
    while True:
        m += 1
        print("m = ", m)
        n = 0
        l = 1
        L = m*l*(m + n)
        M2 = m*m
        if L > 750000:
            break
        while n < m:
            n += 1
            l = 0
            L = 0
            N2 = n*n
            MN2 = 2*m*n
            while L <= 750000:
                l += 1
                L = m*l*(m + n)
                X = (M2 - N2)*l
                Y = MN2*l
                d.setdefault(L, {})
                x = min(X, Y)
                y = max(X, Y)
                if (x > 0) and (y > 0):
                    #dd = d[L].get((x, y), 0)
                    d[L][(x, y)] = 1
    
    w = 0
    for L in d.keys():
        if (L <= 750000) and (len(d[L]) == 1):
            print(d[L])
            w += 1
    print("w = ", w)
