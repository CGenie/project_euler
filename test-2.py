#!/usr/bin/python
# #####################################################################
# test-2.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import unittest

class Test(unittest.TestCase):
    def test0092(self):
        from id_0092 import gennum

        self.assertEqual(gennum(44), 1)
        self.assertEqual(gennum(145), 89)
    
    def test0096(self):
        from id_0096 import row, col, cell, check_table, solve, contains_duplicates, contains_duplicates_set
        from random import randint

        f = open('id_0096-test.txt')
        arr = []
        for line in f:
            arr.append([int(x) for x in line.strip()])
        f.close()
        self.assertEqual(row(arr, 1), [9, 0, 0, 3, 0, 5, 0, 0, 1])
        self.assertEqual(col(arr, 2), [3, 0, 1, 8, 0, 6, 2, 0, 5])
        self.assertEqual(cell(arr, 4), [1, 0, 2, 0, 0, 0, 7, 0, 8])
        self.assertEqual(check_table(arr), True)
        sol = solve(arr)
        f = open('id_0096-test-ans.txt')
        arr_sol = []
        for line in f:
            arr_sol.append([int(x) for x in line.strip()])
        f.close()
        self.assertEqual(sol, arr_sol)

        for n in range(100):
            arr = [randint(1, 9) for x in range(9)]
            self.assertEqual(contains_duplicates(arr), contains_duplicates_set(arr))

    def test0102(self):
        from id_0112 import increasing, decreasing, bouncy
        from random import randint
        
        for x in range(20):
            lst = list(map(lambda x: str(randint(0, 9)), range(7)))
            lst.sort()
            inc = ''.join(lst)
            lst.reverse()
            dec = ''.join(lst)
            self.assertEqual(increasing(inc), True)
            self.assertEqual(decreasing(inc), False)
            self.assertEqual(increasing(dec), False)
            self.assertEqual(decreasing(dec), True)
        self.assertEqual(bouncy(155349), True)
        bnc = 0
        for n in range(1, 1000):
            if bouncy(n):
                bnc += 1
        self.assertEqual(bnc, 525)

    def test0165_1(self):
        from id_0165 import shub

        self.assertEqual([27, 144, 12, 232], [shub(n) for n in [1, 2, 3, 4]])

    def test0165_2(self):
        from id_0165 import Point, Line, sweep_line
        a = Point(27, 44)
        b = Point(12, 32)
        c = Point(46, 53)
        d = Point(17, 62)
        e = Point(46, 70)
        f = Point(22, 40)
        k = Line(a, b)
        l = Line(c, d)
        m = Line(e, f)

        self.assertEqual(sweep_line([k, l, m]), [set([l, m])])

if __name__ == '__main__':
    unittest.main()

