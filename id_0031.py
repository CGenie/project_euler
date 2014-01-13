#!/usr/bin/python2
# #####################################################################
# id_0031.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from copy import deepcopy

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def make_value(val, max_coin_pos = 0, lst = []):
    s = 0
    for i in range(max_coin_pos, len(coins)):
        tmp = deepcopy(lst)
        coin = coins[i]
        if val - coin > 0:
            tmp.append(coin)
            s += make_value(val - coin, max_coin_pos = i, lst = tmp)
        if val - coin == 0:
            tmp.append(coin)
            #print tmp
            s += 1
    return s

if __name__ == '__main__':
    print make_value(200)
