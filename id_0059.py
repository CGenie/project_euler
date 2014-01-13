#!/usr/bin/python2
# #####################################################################
# id_0059.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import cycle, combinations

# combinations don't do repeating, so we do it ourselves
letters = ''.join([chr(x) for x in range(ord('a'), ord('z') + 1)]*3)

def xor_encrypt(enc, key):
    dec = []
    n = 0
    f = cycle(key)
    while n < len(enc):
        k = f.next()
        dec.append(chr(ord(k)^ord(enc[n])))
        n += 1
    return ''.join(dec)

if __name__ == '__main__':    
    words = []
    f = open("/usr/share/dict/cracklib-small")
    for line in f:
        words.append(line.strip())
    f.close()

    oddstuff = ['%', '&', '#', '{', '}', '|', '~']

    f = open("./id_0059.txt")
    enc = []
    for line in f:
        enc.extend(line.strip().split(","))
    enc = ''.join([chr(int(x)) for x in enc])

    for c in combinations(letters, 3):
        dec = xor_encrypt(enc, ''.join(c)).lower()
        # find 5 words from the dict, if so, dec looks suspicious ;)
        suspicious = 0
        is_odd = False
        print "Testing key ::" + ''.join(c) + ":: for suspisciousness..."
        for x in oddstuff:
            idx = dec.find(x)
            if idx > -1:
                is_odd = True
                break
        if is_odd == False:
            for word in words:
                if len(word) > 4:
                    idx = dec.find(word)
                    if idx > -1:
                        print "Word " + str(word) + " found in dec"
                        print "*"*15
                        dec = xor_encrypt(enc, ''.join(c))
                        print dec
                        ss = sum([ord(x) for x in dec])
                        print "The sum is %d" % ss
                        print "*"*15
                        foo = input("Press enter to continue...")
                        break
