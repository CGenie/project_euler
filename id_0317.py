#!/usr/bin/python
# #####################################################################
# id_0317.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import pi, sqrt

if __name__ == '__main__':
    v0 = 20
    g = 9.81
    C = 100 + v0**2/(2*g)
    mu = g/(2*v0**2)
    x0 = sqrt(C/mu)
    print("sol = " + str(0.5*mu*pi*x0**4))
