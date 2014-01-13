#!/usr/bin/python2
# #####################################################################
# id_0068.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import permutations

def check_sums(lst):
    s = sum(lst[0])
    for x in lst:
        if s != sum(x):
            return False
    return True

def fill_n_gon(nums):
    # first n values go outside, the rest is filled inside
    lst = []
    # from nums we can calculate n
    n = len(nums)/2
    for i in range(n):
        lst.append([nums[i], 0, 0])
    for i in range(n, 2*n):
        lst[i - n][2] = nums[i]
        lst[(i + 1 - n) % n][1] = nums[i]
    return lst

def make_num_from_lst(lst):
    first = [x[0] for x in lst]
    m = min(first)
    idx = first.index(m)
    num = []
    for l in range(len(first)):
        i = (idx + l) % len(first)
        num.append(first[i])
        num += lst[i][1:]
    return int(''.join([str(x) for x in num]))

if __name__ == '__main__':
    M = 1
    for first in permutations(range(6, 11)):
        for second in permutations(range(6)):
            nums = first + second
            lst = fill_n_gon(nums)
            if check_sums(lst):
                ret = make_num_from_lst(lst)
                if ret > M:
                    M = ret
                    print "New maximum found: %d" % ret
    print M
