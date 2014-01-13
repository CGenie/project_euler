#!/usr/bin/python
# #####################################################################
# test-2.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import unittest

class Test(unittest.TestCase):
    def test0096(self):
        import time
        from id_0096 import solve

        arr = []
        f = open('id_0096-test.txt')
        for line in f:
            arr.append([int(x) for x in line.strip()])
        f.close()
        start = time.time()
        solve(arr)
        end = time.time()
        print("time taken: ", end - start)

    def test0096_duplicates(self):
        import time
        from id_0096 import contains_duplicates, contains_duplicates_set
        from random import randint
        
        start = time.time()
        for n in range(20000):
            arr = [randint(1, 9) for x in range(9)]
        end = time.time()
        print("time for creating arrays: ", end - start)
        arrtime = end - start

        start = time.time()
        for n in range(20000):
            arr = [randint(1, 9) for x in range(9)]
            contains_duplicates(arr)
        end = time.time()
        print("time for contains_duplicates: ", end - start - arrtime)

        start = time.time()
        for n in range(20000):
            arr = [randint(1, 9) for x in range(9)]
            contains_duplicates_set(arr)
        end = time.time()
        print("time for contains_duplicates_set: ", end - start - arrtime)

    def test0086(self):
        import time

        d_sqr = {1: 1}
        d_sqrt = {1: 1}
        M = 500
        # compute all squares up to 5*M**2, the naive way
        start = time.time()
        for x in range(2, 5*M**2):
            n2 = x**2
            d_sqr[x] = n2
            d_sqrt[n2] = x
        end = time.time()
        print("square computing, time for the naive way: ", end - start)
        # compute squares, the optimized way
        start = time.time()
        for x in range(2, 5*M**2):
            n2 = d_sqr[x] = d_sqr[x - 1] + 2*(x - 1) + 1
            d_sqrt[n2] = x
        end = time.time()
        print("squares computing, time for the optimized way: ", end - start)
        start = time.time()
        for x in range(2, 5*M**2):
            d_sqr[x] = d_sqr[x - 1] + 2*(x - 1) + 1
            d_sqrt[d_sqr[x]] = x
        end = time.time()
        print("squares computing, time for the optimized way 2: ", end - start)
    
        # ownership testing
        d = {}
        for x in range(10**5):
            d[x] = 1
        s = set(d.keys())

        start = time.time()
        for x in range(10**5):
            r = x in d
        end = time.time()
        print("ownership in dictionary: ", end - start)

        start = time.time()
        for x in range(10**5):
            r = x in s
        end = time.time()
        print("ownership in set: ", end - start)

if __name__ == '__main__':
    unittest.main()
