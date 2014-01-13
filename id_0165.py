#!/usr/bin/env python

import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '%s - %s' % (self.a, self.b)

def counter_clockwise(a, b, c):
    return (b.x - a.x)*(c.y - b.y) - (c.x - b.x)*(b.y - a.y) < 0

def segments_intersect(k, l):
    a = k.a
    b = k.b
    c = l.a
    d = l.b
    if counter_clockwise(a, c, d) == counter_clockwise(b, c, d):
        return False
    if counter_clockwise(a, b, c) == counter_clockwise(a, b, d):
        return False
    return True

def prepare_lines(lines):
    ret = []
    for line in lines:
        if line.b.x < line.a.x:
            line.a, line.b = line.b, line.a
        ret.append(line)
    return ret

def check_intersect(l1, l2):
    assert(len(l1) == len(l2))
    ret = []
    for i, line in enumerate(l1):
        if l2[i] != line:
            ret.append(set([line, l2[i]]))
    return ret

def sweep_line(lines):
    intersections = []

    lines = prepare_lines(lines)
    xleft = [line.a.x for line in lines]
    xright = [line.b.x for line in lines]
    m = min(xleft)
    M = max(xright)
    xes = []
    xes.extend(xleft)
    xes.extend(xright)
    xes = list(set(xes))
    xes.sort()
    print(xes)

    tmp = []

    for h in xes:
        for line in lines:
            if line.a.x == h:
                tmp.append(line)
                tmp.sort(key = lambda line: line.a.y)
                print("appending: %s" % str(line))
            if line.b.x == h:
                # check intersections here
                tmp2 = copy.copy(tmp)
                tmp2.sort(key = lambda line: line.b.y)
                intersections.extend(check_intersect(tmp, tmp2))

                tmp.remove(line)
                print("popping: %s" % str(line))
    print("intersections:")
    for line in intersections:
        print(line)
    return intersections

_shubs = {0: 290797}
def shubs(n):
    try:
        return _shubs[n]
    except KeyError:
        _shubs[n] = shubs(n - 1)**2 % 50515093
        return _shubs[n]

_shub = {}
def shub(n):
    try:
        return _shub[n]
    except KeyError:
        _shub[n] = shubs(n) % 500
        return _shub[n]

if __name__ == '__main__':
    pts = [Point(shub(2*n), shub(2*n + 1)) for n in range(10000)]
    lines = [Line(pts[2*i], pts[2*i + 1]) for i in range(5000)]
    print(len(sweep_line(lines)))

