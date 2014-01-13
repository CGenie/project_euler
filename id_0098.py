#!/usr/bin/python2
# #####################################################################
# id_0098.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize
from math import sqrt
import pickle
import os.path
from string import maketrans
from itertools import combinations, permutations

@memoize()
def is_square(n):
    ss = int(sqrt(n))
    return ss*ss == n

@memoize()
def make_sets(arr):
    ret = []
    for x in arr:
        ret.append(set(x))
    return tuple(ret)

def make_anagrams_dict(arr):
    ret = {}
    used_keys = []
    n = len(arr)
    for i, word in enumerate(arr):
        if not word in used_keys:
            ret[word] = []
            used_keys.append(word)
            ss = set(word)
            # generate the dict of letters with their count
            dword = {}
            for x in word:
                try:
                    dword[x] += 1
                except KeyError:
                    dword[x] = 1
            for k in range(i + 1, n):
                ana = arr[k]
                if ss == set(ana):
                    # generate the dict of letters with their count
                    dana = {}
                    for x in ana:
                        try:
                            dana[x] += 1
                        except KeyError:
                            dana[x] = 1
                    anagram = True
                    for x in dana.keys():
                        if dana[x] != dword[x]:
                            anagram = False
                            break
                    if anagram:
                        ret[word].append(ana)
                        used_keys.append(ana)
            print "Anagrams for " + word + ": " + str(ret[word])
    return ret

def gen_trans(letters):
    srange = map(lambda x: str(x), range(10))
    k = len(letters)
    p = permutations(letters)
    for pp in p:
        c = combinations(srange, k)
        for cc in c:
            yield (''.join(pp), ''.join(cc))

def translation_possible(word, num):
    # sanity check
    if len(word) != len(num):
        return False
    n = 0
    d = {}
    while n < len(num):
        try:
            r = d[int(num[n])]
            if word[n] != r:
                return False
        except KeyError:
            d[int(num[n])] = word[n]
            # check all values of the dict to see if the translation is 1-1
            for k, v in d.iteritems():
                if v == word[n] and k != int(num[n]):
                    return False
        n += 1
    return True

def translate(anagram, word, num):
    # prepare the translation dictionary
    d = {}
    for x in range(len(word)):
        d[word[x]] = num[x]
    # make the translation
    ret = ""
    for x in anagram:
        ret += d[x]
    return ret

if __name__ == '__main__':
    f = open("id_0098.txt")
    s = f.read()
    f.close()
    words = tuple(map(lambda x: x[1:-1], s.split(",")))

    squares = map(lambda x: str(x**2), range(1, 10**5))
    # make a list of squares with specific length
    squares_len = {}
    for i in range(1, 15):
        squares_len[i] = []
    for sq in squares:
        squares_len[len(sq)].append(sq)
    #print squares

    anagrams = {}
    if os.path.isfile("id_0098.anagrams.pickle"):
        f = open("id_0098.anagrams.pickle")
        anagrams = pickle.load(f)
        f.close()
    else:
        f = open("id_0098.anagrams.pickle", "wb")
        anagrams = make_anagrams_dict(words)
        pickle.dump(anagrams, f)
        f.close()

    m = 0

    print "Anagram words:"
    for word, lst in anagrams.iteritems():
        if lst:
            print word + ": " + str(lst)

    # check the anagrams
    words = sorted(words, lambda x, y: len(x) - len(y))
    # for word in words:
    #     if word in anagrams.keys() and anagrams[word]:
    #         letters = ''.join(set(word))
    #         n = len(letters)
    #         print "Analyzing " + word + " (len = " + str(n) + ")" + ", anagrams: " + str(anagrams[word])
    #         tr = gen_trans(letters)
    #         for ll, ss in tr:
    #             t = maketrans(ll, ss)
    #             word_t = word.translate(t)
    #             if word_t[0] != '0' and int(word_t) in squares: #is_square(int(word_t)):
    #                 print "Translation: " + ll + "<->" + ss + ": " + word + "<->" + word_t + " is a square"
    #                 for ana in anagrams[word]:
    #                     ana_t = ana.translate(t)
    #                     if ana_t[0] != '0' and int(ana_t) in squares: #is_square(int(ana_t)):
    #                             print "Anagram: " + ana + "<->" + ana_t + " is a square"
    #                             m = max(m, int(ana_t), int(word_t))
    #                             print "Maximal square so far: " + str(m)

    for word in words:
        if word in anagrams.keys() and anagrams[word]:
            letters = ''.join(set(word))
            n = len(letters)
            print "Analyzing " + word + " (len = " + str(n) + "), anagrams: " + str(anagrams[word])
            print str(len(squares_len[len(word)])) + " candidates for squares"
            for sq in squares_len[len(word)]:
                if translation_possible(word, sq):
                    #print "Possibility of translating " + word + " into " + sq
                    # check all anagrams
                    all_possible = True
                    M = int(sq)
                    for ana in anagrams[word]:
                        # translate the anagram
                        #print "Analyzing anagram " + ana
                        ana_tr = translate(ana, word, sq)
                        #print ana_tr
                        if ana_tr in squares:
                            print "Anagram " + ana + " is also a square: " + ana_tr
                            M = max(M, int(ana_tr))
                        else:
                            all_possible = False
                            break
                    if all_possible:
                        m = max(m, M)
                        print "We have a good translation, m = " + str(m)
                        
    print "m = " + str(m)
