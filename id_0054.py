#!/usr/bin/python2
# #####################################################################
# id_0054.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
colors = ['C', 'D', 'H', 'S']

# a hand is a 5-tuple of pairs (card, color)

def parse_hand(ss):
    lst = ss.split(' ')
    return [(x[0], x[1]) for x in lst]

def high_card(hand1, hand2):
    # 1 if player 1, -1 if player 2
    winner = 0
    cards1 = [card for (card, color) in hand1]
    cards2 = [card for (card, color) in hand2]
    for i in range(len(cards) - 1, -1, -1):
        card = cards[i]
        if card in cards1:
            winner = 1
        if card in cards2:
            winner = -1
        if card in cards1 and card in cards2:
            winner = 0
        if winner:
            break
    return winner

def one_pair(hand1, hand2):
    winner = 0
    cards1 = [card for (card, color) in hand1]
    cards2 = [card for (card, color) in hand2]
    d1 = {}
    d2 = {}
    for card in cards:
        d1[card] = d2[card] = 0
    for card in cards1:
        d1[card] += 1
    for card in cards2:
        d2[card] += 1
    for i in range(len(cards) - 1, -1, -1):
        card = cards[i]
        c1 = d1[card]
        c2 = d2[card]
        if c1 == 2:
            winner = 1
        if c2 == 2:
            winner = -1
        if c1 == 2 and c2 == 2:
            winner = 0
        if winner:
            break
    #if winner == 0:
        #winner = high_card(hand1, hand2)
    return winner

def two_pairs(hand1, hand2):
    winner = 0
    cards1 = [card for (card, color) in hand1]
    cards2 = [card for (card, color) in hand2]
    d1 = {}
    d2 = {}
    for card in cards:
        d1[card] = d2[card] = 0
    for card in cards1:
        d1[card] += 1
    for card in cards2:
        d2[card] += 1
    p1 = []
    p2 = []
    for i in range(len(cards) - 1, -1, -1):
        card = cards[i]
        c1 = d1[card]
        c2 = d2[card]
        if c1 == 2:
            p1.append(card)
        if c2 == 2:
            p2.append(card)
    if len(p1) == 2 and len(p2) < 2:
        winner = 1
    if len(p1) < 2 and len(p2) == 2:
        winner = -1
    if len(p1) == 2 and len(p2) == 2:
        h1 = [(p1[0], 'C'), (p1[1], 'C')]
        h2 = [(p2[0], 'C'), (p2[1], 'C')]
        winner = high_card(h1, h2)
    #if winner == 0:
        #winner = high_card(hand1, hand2)
    return winner

def three_of_a_kind(hand1, hand2):
    winner = 0
    cards1 = [card for (card, color) in hand1]
    cards2 = [card for (card, color) in hand2]
    d1 = {}
    d2 = {}
    for card in cards:
        d1[card] = d2[card] = 0
    for card in cards1:
        d1[card] += 1
    for card in cards2:
        d2[card] += 1
    for i in range(len(cards) - 1, -1, -1):
        card = cards[i]
        c1 = d1[card]
        c2 = d2[card]
        if c1 == 3:
            winner = 1
        if c2 == 3:
            winner = -1
        if c1 == 3 and c2 == 3:
            winner = 0
        if winner:
            break
    #if winner == 0:
        #winner = high_card(hand1, hand2)
    return winner

def straight(hand1, hand2):
    winner = 0
    cards1 = [card for (card, color) in hand1]
    cards2 = [card for (card, color) in hand2]
    for i in range(len(cards) - 1, 3, -1):
        straight1 = True
        straight2 = True
        for x in range(5):
            card = cards[i - x]
            if not card in cards1:
                straight1 = False
            if not card in cards2:
                straight2 = False
        if straight1:
            winner = 1
        if straight2:
            winner = -1
        if straight1 and straight2:
            winner = 0
        if winner:
            break
    #if winner == 0:
        #winner = high_card(hand1, hand2)
    return winner

def flush(hand1, hand2):
    winner = 0
    colors1 = [color for (card, color) in hand1]
    colors2 = [color for (card, color) in hand2]
    for i in range(3, -1, -1):
        color = colors[i]
        flush1 = True
        flush2 = True
        for i in range(5):
            if color != colors1[i]:
                flush1 = False
            if color != colors2[i]:
                flush2 = False
        if flush1:
            winner = 1
        if flush2:
            winner = -1
        if flush1 and flush2:
            winner = 0
        if winner:
            break
    #if winner == 0:
        #winner = high_card(hand1, hand2)
    return winner

def full_house(hand1, hand2):
    winner = 0
    cards1 = [card for (card, color) in hand1]
    cards2 = [card for (card, color) in hand2]
    d1 = {}
    d2 = {}
    for card in cards:
        d1[card] = d2[card] = 0
    for card in cards1:
        d1[card] += 1
    for card in cards2:
        d2[card] += 1
    fh1 = {}
    fh2 = {}
    for card in cards:
        c1 = d1[card]
        c2 = d2[card]
        if c1 == 3:
            fh1[3] = card
        if c1 == 2:
            fh1[2] = card
        if c2 == 3:
            fh2[3] = card
        if c2 == 2:
            fh2[2] = card
    if len(fh1.keys()) == 2 and len(fh2.keys()) < 2:
        winner = 1
    if len(fh1.keys()) < 2 and len(fh2.keys()) == 2:
        winner = -1
    if len(fh1.keys()) == 2 and len(fh2.keys()) == 2:
        for i in range(len(cards) - 1, -1, -1):
            card = cards[i]
            if fh1[3] == card:
                winner = 1
            if fh2[3] == card:
                winner = -1
            if fh1[3] == card and fh2[3] == card:
                winner = 0
            if winner:
                break
        if winner == 0:
            for i in range(len(cards) - 1, -1, -1):
                card = cards[i]
                if fh1[2] == card:
                    winner = 1
                if fh2[2] == card:
                    winner = -1
                if fh1[2] == card and fh2[2] == card:
                    winner = 0
                if winner:
                    break
    #if winner == 0:
        #winner = high_card(hand1, hand2)
    return winner

def four_of_a_kind(hand1, hand2):
    winner = 0
    cards1 = [card for (card, color) in hand1]
    cards2 = [card for (card, color) in hand2]
    d1 = {}
    d2 = {}
    for card in cards:
        d1[card] = d2[card] = 0
    for card in cards1:
        d1[card] += 1
    for card in cards2:
        d2[card] += 1
    for i in range(len(cards) - 1, -1, -1):
        card = cards[i]
        if d1[card] == 4:
            winner = 1
        if d2[card] == 4:
            winner = -1
        if d1[card] == 4 and d2[card] == 4:
            winner = 0
            break
        if winner:
            break
    #if winner == 0:
        #winner = high_card(hand1, hand2)
    return winner

def straight_flush(hand1, hand2):
    winner = 0
    cards1 = [card for (card, color) in hand1]
    colors1 = [color for (card, color) in hand1]
    cards2 = [card for (card, color) in hand2]
    colors2 = [color for (card, color) in hand2]
    # first check that the colors match
    has_color1 = (colors1[0] * 5 == ''.join(colors1))
    has_color2 = (colors2[0] * 5 == ''.join(colors2))
    if not has_color1 and not has_color2:
        return 0
    # now check for a straight
    for i in range(len(cards) - 1, 3, -1):
        straight1 = True
        straight2 = True
        color1 = True
        color2 = True
        for x in range(5):
            card = cards[i - x]
            if not card in cards1:
                straight1 = False
            if not card in cards2:
                straight2 = False
        if straight1 and has_color1:
            winner = 1
        if straight2 and has_color2:
            winner = -1
        # if tie then the color decides
        if straight1 and has_color1 and straight2 and has_color2:
            for x in range(len(colors) - 1, -1, -1):
                color = colors[x]
                if colors1[0] == color:
                    winner = 1
                if colors2[0] == color:
                    winner = -1
                if winner:
                    break
        if winner:
            break
    return winner

def decide_winner(hand1, hand2):
    winner = 0
    funcs = [straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, one_pair, high_card]
    for f in funcs:
        winner = f(hand1, hand2)
        if winner:
            print f.__name__
            break
    return winner

if __name__ == '__main__':
    f = open("./id_0054.txt")
    pl1 = 0
    for line in f:
        lst = line.strip().split(" ")
        hand1 = " ".join(lst[:5]).strip()
        hand2 = " ".join(lst[5:]).strip()
        winner = decide_winner(parse_hand(hand1), parse_hand(hand2))
        if winner == 1:
            pl1 += 1
            print "Deal " + hand1 + " ::: " + hand2 + " -- Player 1 wins"
        elif winner == -1:
            print "Deal " + hand1 + " ::: " + hand2 + " -- Player 2 wins"
        else:
            print "Deal " + hand1 + " ::: " + hand2 + " -- A TIE"
    print pl1
