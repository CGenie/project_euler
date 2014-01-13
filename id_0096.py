#!/usr/bin/python
# #####################################################################
# id_0096.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import chain
import copy

def row(arr, k):
    # return the k-th row of array
    return arr[k]

def col(arr, k):
    # return the k-th column of array
    return [arr[j][k] for j in range(9)]

def cell(arr, n):
    # return the n-th cell, as a list
    i = (n % 3)
    j = int((n - i) / 3)
    lst = [[arr[m][n] for n in range(3*j, 3*(j + 1))] for m in range(3*i, 3*(i + 1))]
    return list(chain.from_iterable(lst))
    
def contains_duplicates(lst):
    # checks if a list contains duplicates
    d = {k: 0 for k in range(10)}
    for x in lst:
        d[x] += 1
    for k in d:
        if k != 0 and d[k] > 1:
            return True
    return False

def contains_duplicates_set(lst):
    aa = [x for x in lst if x != 0]
    return len(set(aa)) != len(aa)

def check_table(arr):
    # checks if rows, columns and cells are valid
    # zeros are ignored
    # returns False if table is incorrect
    # first the rows
    for c in range(9):
        if contains_duplicates(cell(arr, c)):
            return False
    for r in range(9):
        if contains_duplicates(row(arr, r)):
            return False
    for c in range(9):
        if contains_duplicates(col(arr, c)):
            return False
    return True

def solve(arr):
    # solve recursively by replacing the first found zero by
    # consecutive integers
    # set arr[0][0] = 0 if not possible to have any integer at this
    # point

    zero_found = False
    # find the first zero
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                zero_found = True
                break
        if zero_found:
            break
    # check if we are done
    if zero_found == False:
        return arr

    arr_mod = None
    for n in range(1, 10):
        # remember the array
        #arr_mod = copy.deepcopy(arr)
        arr_mod = arr
        arr_mod[i][j] = n
        if check_table(arr_mod):
            arr_mod = solve(arr_mod)
            if arr_mod[0][0] != 0:
                return arr_mod
    # incorrect, set first element to 0
    arr_mod[0][0] = 0
    # and set back our element to 0
    arr_mod[i][j] = 0
    return arr_mod

if __name__ == '__main__':
    f = open('id_0096.txt')
    s = 0
    while True:
        # read the next array
        # the title
        try:
            title = next(f).strip()
            print(title)
        except StopIteration:
            break
        # the array
        arr = []
        for n in range(9):
            arr.append([int(x) for x in next(f).strip()])
        sol = solve(arr)
        n = int(''.join([str(x) for x in sol[0]]))
        s += n
    print("ans = ", s)
