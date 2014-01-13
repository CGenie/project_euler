#!/usr/bin/python
# #####################################################################
# id_0084-2.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import random

fields = ('GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
          'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
          'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
          'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2')

ccret = ['GO', 'JAIL', '00', '00', '00', '00', '00', '00',
         '00', '00', '00', '00', '00', '00', '00', '00']

cret = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'RN', 'RN',
        'UN', 'BB3', '00', '00', '00', '00', '00', '00']

d_f2modal = {}
d_modal2f = {}

def gen_dicts():
    for n in range(40):
        d_f2modal[fields[n]] = n
        d_modal2f[n] = fields[n]

def shuffle_cards():
    for n in range(1000):
        r1 = random.randint(0, 15)
        r2 = random.randint(0, 15)
        c = ccret.pop(r1)
        ccret.insert(r2, c)
    for n in range(1000):
        r1 = random.randint(0, 15)
        r2 = random.randint(0, 15)
        c = cret.pop(r1)
        cret.insert(r2, c)
    

def CC():
    """Draw a card from Community Chest"""
    ret = ccret.pop(0)
    ccret.append(ret)
    print("CC card: " + ret)
    return ret

def Chance():
    """Draw a card from Chance"""
    ret = cret.pop(0)
    cret.append(ret)
    print("Chance card: " + ret)
    return ret


def dice():
    return random.randint(1, 4)

double_cnt = 0

def jump(pos):
    global double_cnt
    d1 = dice()
    d2 = dice()
    d = d1 + d2
    if d1 == d2:
        double_cnt += 1
        if double_cnt == 3:
            print("Jump: TRIPLE DOUBLE")
            ret = d_f2modal['JAIL']
            double_cnt = 0
        else:
            ret = (pos + d) % 40
    else:
        double_cnt = 0
        ret = (pos + d) % 40
    field = d_modal2f[ret]
    print("Jump: dice = " + str(d1) + " -- " + str(d2) + ", new position: " + field + "(" + str(d_f2modal[field]).zfill(2) + ")")
    if field[:2] == 'CC':
        cc = CC()
        if cc != '00':
            ret = d_f2modal[cc]
    elif field[:2] == 'CH':
        ch = Chance()
        if ch == 'BB3':
            ret = (pos - 3) % 40
            if d_modal2f[ret] == 'CC':
                cc = CC()
                if cc != '00':
                    ret = d_f2modal[cc]
        elif ch[1] == 'N':
            s = ch[0]
            while True:
                ret = (ret + 1) % 40
                if d_modal2f[ret][0] == s:
                    break
        elif ch != '00':
            ret = d_f2modal[ch]
    elif field == 'G2J':
        ret = d_f2modal['JAIL']
    return ret

d_visited = {}

if __name__ == '__main__':
    double_cnt = 0
    gen_dicts()
    shuffle_cards()

    for n in range(40):
        d_visited[n] = 0

    pos = 0
    cnt = 1
    
    print("CC: " + str(ccret))
    print("Chance: " + str(cret))

    for n in range(250000):
        d_visited[pos] += 1
        cnt += 1
        pos = jump(pos)

    # print statistics
    for n in range(40):
        print("field " + str(n) + " visited " + str(d_visited[n]) + " times")

    vv = list(d_visited.values())
    vv.sort()
    mm = vv[-3:]
    print("max values:")
    for m in mm:
        for n in range(40):
            if d_visited[n] == m:
                print("n = " + str(n) + ", d_visited[n] = " + str(d_visited[n]), ", (" + str(float(d_visited[n]/cnt)) + "%)")

