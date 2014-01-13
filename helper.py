#!/usr/bin/python2
# #####################################################################
# helper.py
# Some helper functions
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def unique(lst, idfun = None):
    """Returns the list with duplicate elements removed. This function
    is order-preserving."""
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in lst:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

def uniqueTrick(lst):
    unique_trick = [ uniq for uniq in lst if uniq not in locals()['_[1]'] ]
    return unique_trick

if __name__ == '__main__':
    # test the speed of the code
    import timeit
    import random

    lst = [random.randint(0, 10) for x in range(1000)]
    tunique = timeit.Timer("unique(lst)", "from __main__ import unique, lst")
    tuniquetrick = timeit.Timer("uniqueTrick(lst)", "from __main__ import uniqueTrick, lst")
    try:
        print tunique.timeit(500)
        print tuniquetrick.timeit(500)
    except:
        tunique.print_exc()
        tuniquetrick.print_exc()
