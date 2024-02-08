import random

def f1(string):
    l = string.split()
    random.shuffle(l)
    return " ".join(l)

def f2(string):
    k = 0
    l = string.split()
    for i in l:
        if len(i) % 2 == 0: k += 1
    return k
