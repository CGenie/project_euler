#!/usr/bin/python
# #####################################################################
# helper_py3.py
# Some helper functions
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import hashlib
import pickle

def compute_key(function, args, kw):
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()

def memoize():
    d_mem = {}
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)
            return d_mem.setdefault(key, function(*args, **kw))
        return __memoize
    return _memoize

class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            return self.func(*args)
    def __repr__(self):
        return self.func.__doc__
    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)
