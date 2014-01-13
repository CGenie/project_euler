#!/usr/bin/python2
# #####################################################################
# id_0060.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import pickle
from itertools import combinations
from id_0003 import is_prime

if __name__ == '__main__':
    f = open("./primes.pickle")
    lst_primes = pickle.load(f)
    f.close()

    n = 0
    # for primes in combinations(lst_primes[1:500], 5):
    #     nice_four = True
    #     if n % 100 == 0:
    #         n = 1
    #         print "Testing " + str(primes)
    #     for doubles in combinations(primes, 2):
    #         p1 = int(''.join([str(doubles[0]), str(doubles[1])]))
    #         p2 = int(''.join([str(doubles[1]), str(doubles[0])]))
    #         if not p1 in lst_primes or not p2 in lst_primes:
    #             nice_four = False
    #             break
    #     if nice_four:
    #         print "A nice five has been found: " + str(primes)
    #         print "The sum is " + str(sum(primes))
    #         foo = input("Press enter to continue...")
    #     n += 1

    join_nums = lambda x, y: int(''.join([str(x), str(y)]))

    for idx, x in enumerate(lst_primes):
        if x > 10000:
            break
    maxidx = idx
    for a in xrange(5, maxidx):
        pa = lst_primes[a]
        for b in xrange(a, maxidx):
            pb = lst_primes[b]
            # check this pair first
            pab = join_nums(pa, pb)
            pba = join_nums(pb, pa)
            #if pab in lst_primes and pba in lst_primes:
            if is_prime(pab) and is_prime(pba):
                print "%d, %d ok so far..." % (pa, pb)
                for c in xrange(b, maxidx):
                    pc = lst_primes[c]
                    pac = join_nums(pa, pc)
                    pca = join_nums(pc, pa)
                    pbc = join_nums(pb, pc)
                    pcb = join_nums(pc, pb)
                    #print "Testing %d with pac = %d, pca = %d, pbc = %d, pcb = %d" % (pc, pac, pca, pbc, pcb)
                    #if pac in lst_primes and pca in lst_primes and pbc in lst_primes and pcb in lst_primes:
                    if is_prime(pac) and is_prime(pca) and is_prime(pbc) and is_prime(pcb):
                        print "%d, %d, %d ok so far..." % (pa, pb, pc)
                        for d in xrange(c, maxidx):
                            nice_four = True
                            pd = lst_primes[d]
                            pad = join_nums(pa, pd)
                            pda = join_nums(pd, pa)
                            pbd = join_nums(pb, pd)
                            pdb = join_nums(pd, pb)
                            pcd = join_nums(pc, pd)
                            pdc = join_nums(pd, pc)
                            #print "pad = %d, pda = %d, pbd = %d, pdb = %d, pcd = %d, pdc = %d" % (pad, pda, pbd, pdb, pcd, pdc)
                            for pp in [pad, pda, pbd, pdb, pcd, pdc]:
                                #if not pp in lst_primes:
                                if not is_prime(pp):
                                    nice_four = False
                                    break
                            if nice_four:
                                print "%d, %d, %d, %d ok so far..." % (pa, pb, pc, pd)
                                for e in xrange(d, maxidx):
                                    nice_five = True
                                    pe = lst_primes[e]
                                    pae = join_nums(pa, pe)
                                    pea = join_nums(pe, pa)
                                    pbe = join_nums(pb, pe)
                                    peb = join_nums(pe, pb)
                                    pce = join_nums(pc, pe)
                                    pec = join_nums(pe, pc)
                                    pde = join_nums(pd, pe)
                                    ped = join_nums(pe, pd)
                                    for pp in [pae, pea, pbe, peb, pce, pec, pde, ped]:
                                        #if not pp in lst_primes:
                                        if not is_prime(pp):
                                            nice_five = False
                                            break
                                    if nice_five:
                                        print "A nice five has been found: %d, %d, %d, %d, %d" % (pa, pb, pc, pd, pe)
                                        print "The sum is " + str(sum([pa, pb, pc, pd, pe]))
                                        foo = input("Press enter to continue...")
                            
