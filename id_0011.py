#!/usr/bin/python2
# #####################################################################
# id_0011.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0008 import mul

mtrx = []

prod = 0
prod_row = 0
prod_col = 0
prod_direction = ""
prod_lst = []

f = open("./id_0011.txt")

for line in f:
    mtrx.append([int(x) for x in line.strip().split(" ")])

def search_down():
    global prod
    global prod_row
    global prod_col
    global prod_direction
    global prod_lst
    for j in range(20):
        for i in range(16):
            lst = [mtrx[i + x][j] for x in range(4)]
            m = mul(lst)
            if m > prod:
                prod = m
                prod_row = i
                prod_col = j
                prod_direction = "down"
                prod_lst = lst

def search_right():
    global prod
    global prod_row
    global prod_col
    global prod_direction
    global prod_lst
    for i in range(20):
        for j in range(16):
            lst = [mtrx[i][j + x] for x in range(4)]
            m = mul(lst)
            if m > prod:
                prod = m
                prod_row = i
                prod_col = j
                prod_direction = "right"
                prod_lst = lst

def search_down_right():
    global prod
    global prod_row
    global prod_col
    global prod_direction
    global prod_lst
    for i in range(16):
        for j in range(16):
            lst = [mtrx[i + x][j + x] for x in range(4)]
            m = mul(lst)
            if m > prod:
                prod = m
                prod_row = i
                prod_col = j
                prod_direction = "down-right"
                prod_lst = lst

def search_up_right():
    global prod
    global prod_row
    global prod_col
    global prod_direction
    global prod_lst
    for i in range(16):
        for j in range(3, 20):
            lst = [mtrx[i + x][j - x] for x in range(4)]
            m = mul(lst)
            if m > prod:
                prod = m
                prod_row = i
                prod_col = j
                prod_direction = "up-right"
                prod_lst = lst

search_down()
search_right()
search_down_right()
search_up_right()

print prod
print prod_row, prod_col
print prod_direction
print prod_lst
