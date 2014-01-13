#!/usr/bin/python
# #####################################################################
# id_0096-2.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def product(A, B):
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = product(rows, cols)
unitlist = ([product(rows, c) for c in cols] +
            [product(r, cols) for r in rows] +
            [product(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) 
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

def parse_grid(grid):
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(grid).items():
        #values[s] = d
        if d in digits and not assign(values, s, d):
            return False
    return values

def grid_values(grid):
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

def pretty_print(v):
    for r in rows:
        ss = ' '.join(v[r+c] for c in cols)
        print(ss)

def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

def solve(grid):
    return search(parse_grid(grid))

def search(values):
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares): 
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) 
                for d in values[s])

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

f = open('id_0096.txt')
s = 0
while True:
    try:
        line = next(f).strip()
        print(line)
    except StopIteration:
        break
    arr = []
    for x in range(9):
        arr.append(next(f).strip())
    ss = ''.join(arr)
    ans = solve(ss)
    pretty_print(ans)
    print(''.join(ans['A' + c] for c in '123'))
    s += int(''.join(ans['A' + c] for c in '123'))
print("ans = ", s)
