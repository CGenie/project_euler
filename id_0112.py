#!/usr/bin/python
# #####################################################################
# id_0112.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

#d_inc = {}
#d_dec = {}
#d_bnc = {}

# def increasing(s):
#     try:
#         return d_inc[s]
#     except KeyError:
#         if len(s) == 1:
#             d_inc[s] = True
#         else:
#             if (int(s[0]) <= int(s[1])) and increasing(s[1:]):
#                 d_inc[s] = True
#             else:
#                 d_inc[s] = False
#         return d_inc[s]

@memoize()
def increasing(s):
    if len(s) == 1:
        return True
    else:
        if(int(s[0]) <= int(s[1])) and increasing(s[1:]):
            return True
        else:
            return False

# def decreasing(s):
#     try:
#         return d_dec[s]
#     except KeyError:
#         if len(s) == 1:
#             d_dec[s] = True
#         else:
#             if (int(s[0]) >= int(s[1])) and decreasing(s[1:]):
#                 d_dec[s] = True
#             else:
#                 d_dec[s] = False
#         return d_dec[s]

@memoize()
def decreasing(s):
    if len(s) == 1:
        return True
    else:
        if (int(s[0]) >= int(s[1])) and decreasing(s[1:]):
            return True
        else:
            return False

def bouncy(n):
    return not (increasing(str(n)) or decreasing(str(n)))

if __name__ == '__main__':
    bnc = 0
    n = 1
    while True:
        if bouncy(n):
            bnc += 1
            if bnc % 100000 == 0:
                print("n = ", n, ", bnc = ", bnc, ", bnc/n = ", float(bnc)/n)
        if 100*bnc == 99*n:
            break
        n += 1
    print("n = ", n)
    
