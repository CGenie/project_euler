#!/usr/bin/python
# #####################################################################
# id_0085.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def genprimes():
    arr = [2]
    yield 2
    s = 2
    while True:
        s += 1
        is_prime = True
        for x in arr:
            if s % x == 0:
                is_prime = False
                break
        if is_prime:
            arr.append(s)
            yield s

if __name__ == '__main__':
    d = {}
    M = 50*(10**6)
    P1 = genprimes()
    while True:
        p1 = P1.next()
        print p1
        s1 = p1**4
        if s1 >= M:
            break
        P2 = genprimes()
        while True:
            p2 = P2.next()
            s2 = p2**3
            S2 = s1 + s2
            if S2 >= M:
                break
            P3 = genprimes()
            while True:
                p3 = P3.next()
                s3 = p3**2
                S3 = S2 + s3
                if S3 >= M:
                    break
                d[S3] = 1
                #print S3
    print "ans = " + str(len(d.keys()))
