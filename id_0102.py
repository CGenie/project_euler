#!/usr/bin/python
# #####################################################################
# id_0102.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def vec(A, B):
    return [A[0] - B[0], A[1] - B[1]]

def scalar_product(u, v):
    return u[0]*v[0] + u[1]*v[1]

# this is wrong...
def contains_origin(A, B, C):
    AB = vec(A, B)
    BC = vec(B, C)
    CA = vec(C, A)
    s1 = scalar_product(AB, A)
    s2 = scalar_product(BC, B)
    s3 = scalar_product(CA, C)
    if  (s1 >= 0) and (s2 >= 0) and (s3 >= 0)                                            :
        return True
    else:
        return False

def cross_prod_third(u, v):
    return u[0]*v[1] - u[1]*v[0]

def abs(m):
    return max(m, -m)

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def contains_origin2(A, B, C):
    AB = vec(A, B)
    BC = vec(B, C)
    CA = vec(C, A)
    s1 = cross_prod_third(AB, A)
    s2 = cross_prod_third(BC, B)
    s3 = cross_prod_third(CA, C)
    l = abs(sum(map(sign, [s1, s2, s3])))
    if l == 3:
        return True
    else:
        return False

if __name__ == '__main__':
    s = 0
    file = open('id_0102.txt')
    for line in file:
        pts = line.strip().split(',')
        ii = lambda x: int(x)
        A = tuple(map(ii, pts[0:2]))
        B = tuple(map(ii, pts[2:4]))
        C = tuple(map(ii, pts[4:6]))
        if contains_origin2(A, B, C):
            s += 1
            print(A, B, C)
    print("ans = ", s)
