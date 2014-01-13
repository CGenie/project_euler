#!/usr/bin/python2
# #####################################################################
# id_0036.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def is_palindrome(s):
    l = len(s)
    n = l/2
    if l % 2 == 1:
        n += 1
    for x in range(n):
        if s[x] != s[-x - 1]:
            return False
    return True

base_k = {}

def to_base_k(num, k):
    try:
        return base_k[(num, k)]
    except KeyError:
        if num == 0:
            base_k[(0, k)] = ""
        else:
            r = num % k
            d = num/k
            base_k[(num, k)] = to_base_k(d, k) + str(r)
        return base_k[(num, k)]

if __name__ == '__main__':
    s = 0
    for x in range(1, 10**6, 2):
        if is_palindrome(str(x)) and is_palindrome(to_base_k(x, 2)):
            s += x
    print s
