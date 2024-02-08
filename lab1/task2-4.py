import random

def f1(string):
    l = string.split()
    random.shuffle(l)
    return " ".join(l)
