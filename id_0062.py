#!/usr/bin/python2
# #####################################################################
# id_0062.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def find_cubes():
    # find cubes between 10**8 and 10**9
    n = 210
    ret = []
    while True:
        r = n**3
        if r > 10**11 - 1 and r < 10**12:
            ret.append(r)
        if r >= 10**12:
            break
        n += 1
    return ret

# num2 is permutation of num1 if they have the same length and same
# digits, counting multiples
def is_permutation(num1, num2):
    s1 = str(num1)
    s2 = str(num2)
    if len(s1) != len(s2):
        return False
    d1 = {}
    d2 = {}
    for x in [str(y) for y in range(10)]:
        d1[x] = 0
        d2[x] = 0
    for x in s1:
        d1[x] += 1
    for x in s2:
        d2[x] += 1
    for k in [str(y) for y in range(10)]:
        if d1[k] != d2[k]:
            return False
    return True
    
if __name__ == '__main__':
    cubes = find_cubes()
    print len(cubes)
    for i in range(len(cubes)):
        if i % 10 == 0:
            print i
        num1 = cubes[i]
        for j in range(i + 1, len(cubes)):
            num2 = cubes[j]
            if is_permutation(num1, num2):
                print num1, num2
                for k in range(j + 1, len(cubes)):
                    num3 = cubes[k]
                    if is_permutation(num1, num3):
                        print num1, num2, num3
                        for l in range(k + 1, len(cubes)):
                            num4 = cubes[l]
                            if is_permutation(num1, num4):
                                print num1, num2, num3, num4
                                for m in range(l + 1, len(cubes)):
                                    num5 = cubes[m]
                                    if is_permutation(num1, num5):
                                        print "Success!!!!"
                                        print num1, num2, num3, num4 
                                        print num1**(1./3)
                                        raise Error
