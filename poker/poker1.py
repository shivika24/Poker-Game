def straight(ranks):                                                       #ranks are a list of numbers
    if len(set(ranks))==5 and max(ranks)-min(ranks)==4:
        return True
    return False

def flush(suits):
    if len(set(suits))==1:
        return True
    return False

def kind(n, ranks):                                                        #n for 3 of a kind or 4 of a kind
    for i in ranks:                                                        #problem with set is it is unordered
        if ranks.count(i)==n:
            return i
    return None

def two_pair(ranks):
    hicard=kind(2,ranks)
    locard=kind(2,tuple(reversed(ranks)))
    if hicard != locard:
        return (hicard, locard)
    return None

def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

def card_suits(hand):
    return [s for r,s in hand]

def poker(hands):
    return max(hands,key=hand_rank)
#max func automatically passes hands as an argument  ,hand_rank is reducing an object to number

def hand_rank(hand):
    ranks = card_ranks(hand)
    suits = card_suits(hand)
    if straight(ranks) and flush(suits):
        return (8, max(ranks))                                          #there was 8 rules
    if kind(4, ranks):
        return(7, kind(4, ranks), kind(1, ranks))        #4 of a kind no. and 5th card number is stored to compare
    if kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    if flush(hand):
        return (5, ranks)
    if straight(ranks):
        return (4, max(ranks))
    if kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    if two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    if kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0,max(ranks))

def check(user,comp):
    cards=[user,comp]
    return poker(cards)
