#!/usr/bin/python
# #####################################################################
# id_0089.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
rules = (("M", 1000),
         ("CM", 900),
         ("D", 500),
         ("CD", 400),
         ("C", 100),
         ("XC", 90),
         ("L", 50),
         ("XL", 40),
         ("X", 10),
         ("IX", 9),
         ("V", 5),
         ("IV", 4),
         ("I", 1),
         )

# make a number out of a roman numeral
def num_from_roman(roman):
    #print("Roman: " + roman)
    num = 0
    idx = 0
    for ch, n in rules:
        while True:
            ll = len(ch)
            if roman[idx:idx + ll] == ch:
                num += n
            else:
                break
            idx += ll
    
    if roman[idx:]:
        print("!! " + roman[idx:] + " !!")
    return num

# make a roman numeral out of a number
def roman_from_num(num):
    s = ""
    for ch, n in rules:
        while True:
            if num >= n:
                s += ch
                num -= n
            else:
                break
    return s

if __name__ == '__main__':
    saved = 0
    f = open("id_0089.txt")
    for l in f:
        r = l.strip()
        nr = num_from_roman(r)
        rn = roman_from_num(nr)
        print("Roman: " + r + " = " + str(nr) + " = " + rn)
        assert(nr == num_from_roman(rn))
        saved += len(r) - len(rn)
    f.close()
    print("sol = " + str(saved))
