#!/usr/bin/python2
# #####################################################################
# id_0026.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from decimal import *

def generate_digits(n):
    s = Decimal(1)/n
    tol = Decimal(10)**-10
    i = 0
    # find the first non-zero digit
    while True:
        if (10**i)*s > 1:
            break
        i += 1
    v = Decimal(0)
    while True:
        r = ((10**i)/n) % 10
        yield r
        v += (Decimal(10)**(-i))*r
        if abs((10**i)*(v - s)) < tol:
            break
        i += 1
        
def has_cycle_len_k(lst, k):
    l = len(lst)
    if l < 2*k:
        return (False, 0)
    for i in range(l - 2*k + 1):
        j = i + k
        mark = True
        pos = i
        for x in range(k):
            if lst[i + x] != lst[j + x]:
                mark = False
                break
        if mark:
            return (True, pos)
    return (False, 0)

def has_cycle(lst, start_k = 1):
    l = len(lst)
    for k in range(start_k, l):
        ret = has_cycle_len_k(lst, k)
        if ret[0]:
            return (k, ret[1])
    return (0, 0)

def cycle_n(n):
    lst = []
    #f = generate_digits(n)
    prec = 50
    getcontext().prec = prec
    tol = 1E-7
    start_k = 1
    #stop = False
    #ret = 0
    #while True:
        #for x in range(100):
            #try:
            #    p = f.next()
            #    lst.append(p)
            #except StopIteration:
            #    stop = True
            #    break
        #ret = has_cycle(lst)
        #if ret > 0 or stop:
            #break
    while True:
        s = Decimal(1)/n
        ss = str(s)
        ss = ''.join(ss.split("."))
        ret = has_cycle(ss, start_k = start_k)
        # now check the result, i.e. if it's really a cycle and nothing shorter
        # else we will compute again, increasing precision
        # first take out all numbers left from our cycle, we don't need them
        # as we're interested only in the cycle itself
        s = Decimal(1)/n
        v = s*(10**ret[1]) % 1
        # now check if it's really a cycle
        c = int(v*(10**ret[0]))
        #print "s = " + str(s) + ", v = " + str(v) + ", c = " + str(c)
        if ret[0] == 0:
            # check if the precision was not sufficient or just our number
            # has a finite number of digits
            if len(ss) < prec:
                break
        else:        
            if abs(v - c/(Decimal(10)**ret[0] - 1)) < Decimal(10)**(-2*ret[0] - 6):
                #print "Cycle is OK, ret = " + str(ret)
                return ret[0]
        start_k = ret[0] + 1
        prec = prec*2
        getcontext().prec = prec
    return ret[0]

if __name__ == '__main__':
    M = 0
    iM = 0
    for i in range(990, 980, -1):
        r = cycle_n(i)
        if r >= M:
            M = r
            iM = i
            print "n = " + str(i) + " has cycle of length " + str(r)
        if i % 10 == 0:
            print "n = " + str(i) + " has cycle of length " + str(r)
    print iM, M
