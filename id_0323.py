#!/usr/bin/python
# #####################################################################
# id_0323.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize
from numpy import *
from numpy import linalg

K = 32

@memoize()
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n - 1)

@memoize()
def binomial(n, k):
    return factorial(n)/(factorial(n - k)*factorial(k))

@memoize()
def p(l, k):
    if l > k:
        return 0.
    return binomial(K - l, k - l)/(2**(K - l))

if __name__ == '__main__':
    A = zeros((K + 1, K + 1))
    for i in range(K + 1):
        for j in range(K + 1):
            A[i, j] = p(i, j)
    p = zeros(K)
    # warunek poczatkowy: x_0 = 0
    p[0] = 1
    # warunek koncowy: p[K]
    #print(A)
    B = A[0:K, 0:K]
    #print(B)
    I = identity(K)
    C = linalg.inv(I - B)
    #print(C)
    oo = ones(K)
    print(dot(C, oo)[0])
