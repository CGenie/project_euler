#!/usr/bin/python
# #####################################################################
# id_0093.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize
from itertools import permutations, product

symbols = "+-*/"

def combinations_with_replacement(iterable, r):
    for pp in product(iterable, repeat = r):
        yield pp

def eval_seq(dig, sym):
    ret = int(dig[0])
    for i in range(3):
        if sym[i] != "/" or ret % int(dig[i + 1]) == 0:
            ret = eval(str(ret) + sym[i] + dig[i + 1])
        else:
            return ""
    return ret

def eval_dig(dig):
    global symbols

    ret = set()
    pp = permutations(dig)
    for p in pp:
        cc = combinations_with_replacement(symbols, 3)
        for c in cc:
            r = eval_seq(p, c)
            if r:
                ret.add(max(0, r))
        # we miss out numbers of form (a x b) */ (c x d)
        for s1 in symbols:
            r1 = 0
            r2 = 0
            if s1 != "/" or int(p[0]) % int(p[1]) == 0:
                r1 = eval(p[0] + s1 + p[1])
            for s2 in symbols:
                if s2 != "/" or int(p[2]) % int(p[2]) == 0:
                    r2 = eval(p[2] + s2 + p[3])
                ret.add(max(0, r1*r2))
                if r2 != 0 and r1 % r2 == 0:
                    ret.add(max(0, r1/r2))
                
    ret.remove(0)
    return ret

def check_seq(dig):
    aa = eval_dig(dig)
    n = 0
    while True:
        n += 1
        if not n in aa:
            break
    return n - 1

if __name__ == '__main__':
    m = 0
    ssf = lambda x: str(x)
    #print filter(lambda x: x > 0, eval_dig(('1', '2', '3', '4')))
    #print len(filter(lambda x: x > 0, eval_dig(('1', '2', '3', '4'))))
    #print eval_dig(('1', '2', '5', '6'))
    print eval_dig(('1', '2', '5', '8'))
    print check_seq(('1', '2', '5', '8'))
    print check_seq(('1', '2', '5', '6'))
    for a in map(ssf, range(1, 7)):
        print "a = " + a
        for b in map(ssf, range(int(a), 8)):
            print "b = " + b
            for c in map(ssf, range(int(b), 9)):
                for d in map(ssf, range(int(c), 10)):
                    r = check_seq((a, b, c, d))
                    if m < r:
                        m = r
                        print a + ", " + b + ", " + c + ", " + d + ": " + str(m)
    print "sol = " + str(m)
