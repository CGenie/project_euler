#!/usr/bin/python2
# #####################################################################
# id_0201.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import combinations

def U(A, k):
    s = []
    d = {}
    for c in combinations(A, k):
        try:
            tst = d[sum(c)]
            if sum(c) in s:
                s.remove(sum(c))
        except KeyError:
            d[sum(c)] = 1
            s.append(sum(c))
    print s
    print sum(s)
    return s

sums_k = {}

def U2_helper(A, k, sum_so_far = {}):
    #global sums_k
    #sums = {}
    if k == 0:
        for key, value in sum_so_far.itertools():
            if value == 1:
                yield key
    else:
        for i in range(len(A) - k + 1):
            el = A[i]
            for key in sum_so_far.keys():
                sum_so_far[key + el] = sum_so_far.get(key + el, 0) + 1
            #curr_sum = sum_so_far + el
            #sums[curr_sum] = sums.get(curr_sum, 0) + 1
            #sums_k[(k, curr_sum)] = sums_k.get((k, curr_sum), 0) + 1
        for i in range(len(A) - k + 1):
            el = A[i]
            curr_sum = sum_so_far + el
            if sums[curr_sum] == 1 and sums_k[(k, curr_sum)] == 1:
                if k in range(5, 51):
                    print "Taking element %d, k = %d" % (el, k)
                print "Calling U2_helper with A = " + str(A[i + 1:]) + ", k = " + str(k - 1), ", sum_so_far = " + str(curr_sum)
                f = U2_helper(A[i + 1:], k - 1, sum_so_far = curr_sum)
                while True:
                    try:
                        ret = f.next()
                        print 'yielding ' + str(ret) + " with A = " + str(A)
                        yield ret
                    except StopIteration:
                        break

def U2(A, k):
    sums = {}
    f = U2_helper(A, k)
    while True:
        try:
            ret = f.next()
            sums[ret] = sums.get(ret, 0) + 1
        except StopIteration:
            break
    s = 0
    for k, v in sums.iteritems():
        if v == 1:
            s += k
    #print sums
    return s

if __name__ == '__main__':
    #S = [x**2 for x in range(1, 101)]
    #lst = U(S, 50)
    #print sum(lst)
    #print U2(S, 50)

    ret = []
    S = [x**2 for x in range(1, 7)]
    cc = combinations(S, 4)
    for c in cc:
        print str(c) + ": " + str(sum(c))
        ret.append(sum(c))
    ret.sort()
    print ret
