#!/usr/bin/python
# #####################################################################
# id_0315.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

digits = {0: (1, 1, 1, 0, 1, 1, 1),
          1: (0, 0, 1, 0, 0, 1, 0),
          2: (1, 0, 1, 1, 1, 0, 1),
          3: (1, 0, 1, 1, 0, 1, 1),
          4: (0, 1, 1, 1, 0, 1, 0),
          5: (1, 1, 0, 1, 0, 1, 1),
          6: (1, 1, 0, 1, 1, 1, 1),
          7: (1, 1, 1, 0, 0, 1, 0),
          8: (1, 1, 1, 1, 1, 1, 1),
          9: (1, 1, 1, 1, 0, 1, 1),
          -1: (0, 0, 0, 0, 0, 0, 0)}

def print_digit(d):
    dd = digits[d]
    if dd[0] == 1:
        print(" ---- ")
    else:
        print("      ")
    s = ""
    if dd[1] == 1:
        s  = "|    "
    else:
        s = "     "
    if dd[2] == 1:
        print(s + "|")
    else:
        print(s + " ")
    if dd[3] == 1:
        print(" ---- ")
    else:
        print("      ")
    if dd[4] == 1:
        s  = "|    "
    else:
        s = "     "
    if dd[5] == 1:
        print(s + "|")
    else:
        print(s + " ")
    if dd[6] == 1:
        print(" ---- ")
    else:
        print("      ")
    

@memoize()
def digital_root(num):
    return sum(map(lambda x: int(x), str(num)))

def digital_root_iterator(num):
    n = num
    yield num
    while True:
        n = digital_root(n)
        if n > 9:
            yield n
        else:
            yield n
            break

d_cost_sam = {}
d_cost_max = {}

def calculate_sam_transition_cost():
    global d_cost_sam

    for x in range(-1, 10):
        for y in range(-1, 10):
            d_cost_sam[(x, y)] = sum(digits[x]) + sum(digits[y])

def calculate_max_transition_cost():
    global d_cost_max

    for x in range(-1, 10):
        for y in range(-1, 10):
            # get the number of common turned-on nodes
            ncommon = 0
            for i in range(7):
                if digits[x][i] == 1 and digits[x][i] == digits[y][i]:
                    ncommon += 1
            xnodes = sum(digits[x])
            ynodes = sum(digits[y])
            d_cost_max[(x, y)] = xnodes + ynodes - 2*ncommon

@memoize()
def transition_cost(num1, num2, sam_max):
    global d_cost_sam
    global d_cost_max

    dd = {}
    if sam_max == "sam":
        dd = d_cost_sam
    else:
        dd = d_cost_max

    if num1 == -1:
        n2 = list(map(lambda x: int(x), str(num2)))
        l2 = len(n2)
        return sum(map(lambda i: dd[(-1, n2[i])], range(l2)))
    if num2 == -1:
        n1 = list(map(lambda x: int(x), str(num1)))
        l1 = len(n1)
        return sum(map(lambda i: dd[(n1[i], -1)], range(l1)))

    n1 = list(map(lambda x: int(x), str(num1)))
    n2 = list(map(lambda x: int(x), str(num2)))

    l1 = len(n1)
    l2 = len(n2)

    if l1 > l2:
        for x in range(l1 - l2):
            n2.insert(0, -1)
    if l2 > l1:
        for x in range(l2 - l1):
            n2.insert(0, -1)

    return sum(map(lambda i: dd[(n1[i], n2[i])], range(max(l1, l2))))

def sam_root_transition_cost(num):
    f = digital_root_iterator(num)
    ret = 0
    arr = [-1]
    for x in f:
        arr.append(x)
    arr.append(-1)
    for i in range(len(arr) - 1):
        ret += transition_cost(arr[i], arr[i + 1], "sam")
    return ret

def max_root_transition_cost(num):
    f = digital_root_iterator(num)
    ret = 0
    arr = [-1]
    for x in f:
        arr.append(x)
    arr.append(-1)
    for i in range(len(arr) - 1):
        ret += transition_cost(arr[i], arr[i + 1], "max")
    return ret

if __name__ == '__main__':
    calculate_sam_transition_cost()
    calculate_max_transition_cost()

    f = open("id_0315.txt")
    primes = []
    for l in f:
        primes.append(int(l))
    f.close()

    print(len(primes))

    s = 0
    n = 0
    for p in primes:
        if n % 1000 == 0:
            print("n = " + str(n) + ", p = " + str(p))
        s += sam_root_transition_cost(p) - max_root_transition_cost(p)
        n += 1
    print("sol = " + str(s))
