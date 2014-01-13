#!/usr/bin/python2
# #####################################################################
# id_0061.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from copy import deepcopy
from itertools import permutations

def generate_list(fun):
    n = 1
    ret = []
    while True:
        r = fun(n)
        if r > 999 and r < 10000:
            ret.append(r)
        elif r >= 10000:
            break
        n += 1
    return ret

def generate_triangles():
    # generate a list of 4-digit triangle numbers
    fun = lambda n: n*(n + 1)/2
    return generate_list(fun)

def generate_square():
    fun = lambda n: n*n
    return generate_list(fun)

def generate_pentagonal():
    fun = lambda n: n*(3*n - 1)/2
    return generate_list(fun)

def generate_hexagonal():
    fun = lambda n: n*(2*n - 1)
    return generate_list(fun)

def generate_heptagonal():
    fun = lambda n: n*(5*n - 3)/2
    return generate_list(fun)

def generate_octagonal():
    fun = lambda n: n*(3*n - 2)
    return generate_list(fun)

def is_cyclic(lst):
    # check if the numbers in the list form a cyclic set
    # these are assumed to be 4-digit numbers
    ss = [str(num) for num in lst]
    if ss[0][:2] != ss[-1][2:]:
        return False
    for i in range(len(ss) - 1):
        if ss[i][2:] != ss[i + 1][:2]:
            return False
    return True

def find_good_pairs(num, lst):
    # finds numbers in lst which have 2 first digits the same as num's 2 last digits
    r = str(num)[2:]
    ss = [str(n) for n in lst]
    ret = []
    for x in ss:
        if r == x[:2]:
            ret.append(int(x))
    return ret

def find_cyclic_nums(lst):
    n = len(lst)
    if n == 0:
        yield []
    if n == 1:
        for el in lst[0]:
            yield [el]
    if n > 1:
        for num in lst[0]:
            r = find_good_pairs(num, lst[1])
            if r:
                w = [r]
                w.extend(lst[2:])
                p = find_cyclic_nums(w)
                while True:
                    try:
                        ret = [num]
                        rr = p.next()
                        ret.extend(rr)
                        yield ret
                    except StopIteration:
                        break
                
if __name__ == '__main__':
    tri = generate_triangles()
    squ = generate_square()
    pen = generate_pentagonal()
    hxg = generate_hexagonal()
    hpg = generate_heptagonal()
    otg = generate_octagonal()
    for p in permutations([tri, squ, pen, hxg, hpg, otg]):
        ret = find_cyclic_nums(p)
        while True:
            try:
                r = ret.next()
                if r and len(r) >= 6 and str(r[0])[:2] == str(r[-1])[2:]:
                    print r
                    print sum(r)
            except StopIteration:
                break
