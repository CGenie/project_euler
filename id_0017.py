#!/usr/bin/python2
# #####################################################################
# id_0017.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def write_number(n):
    numbers = {1: 'one',
               2: 'two',
               3: 'three',
               4: 'four',
               5: 'five',
               6: 'six',
               7: 'seven',
               8: 'eight',
               9: 'nine',
               10: 'ten',
               11: 'eleven',
               12: 'twelve',
               13: 'thirteen',
               14: 'fourteen',
               15: 'fifteen',
               16: 'sixteen',
               17: 'seventeen',
               18: 'eighteen',
               19: 'nineteen',
               20: 'twenty',
               30: 'thirty',
               40: 'forty',
               50: 'fifty',
               60: 'sixty',
               70: 'seventy',
               80: 'eighty',
               90: 'ninety',
               100: 'hundred'
               }
    if n <= 20:
        return numbers[n]
    if 20 < n <= 99:
        s = str(n)
        D = int(s[0])
        d = int(s[1])
        r = numbers[D*10]
        if d > 0:
            r += numbers[d]
        return r
    if 99 < n <= 999:
        s = str(n)
        h = int(s[0])
        D = int(s[1])
        d = int(s[2])
        r = numbers[h] + numbers[100]
        if D*10 + d > 0:
            r += "and" + write_number(D*10 + d)
        return r
    if n == 1000:
        return 'onethousand'

if __name__ == '__main__':
    l = 0
    for x in range(1, 1001):
        print "x = " + str(x) + ", write_number = " + write_number(x)
        l += len(write_number(x))
    print l
