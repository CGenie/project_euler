#!/usr/bin/python2
# #####################################################################
# id_0051.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import pickle
from itertools import combinations

f = open("primes.pickle")
lst_primes = pickle.load(f)
f.close()

def replace_k_digits(num, k):
    ss = str(num)
    cc = range(len(ss))
    for c in combinations(cc, k):
        tmp = [x for x in str(num)]
        for i in xrange(10):
            for d in c:
                tmp[d] = str(i)
            s = ''.join(tmp)
            if len(str(int(s))) == len(tmp):
                yield int(s)
        yield -1
        

def has_k_primes_generated(num, k):
    cnt = 0
    f = replace_k_digits(num, k)
    m = 0
    while True:
        try:
            ret = f.next()
            if ret in lst_primes:
                #print ret
                cnt += 1
            if ret == -1:
                #print "Combination change"
                if m < cnt:
                    m = cnt
                cnt = 0
        except StopIteration:
            break
    return m

if __name__ == '__main__':
    #s = 56003
    ss = 57860
    for i, s in enumerate(lst_primes):
        for k in xrange(1, len(str(s)) - 1):
            if s > ss:
                ret = has_k_primes_generated(s, k)
                if ret == 8:
                    print "%d has 8 primes, k = %d" % (s, k)
                    break
        if i % 10 == 0:
            print "s = %d" % s
