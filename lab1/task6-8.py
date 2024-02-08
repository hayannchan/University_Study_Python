def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def f1(string):
    k = 0
    for c in string:
        if c in range_char("А","я"): k += 1
    return k

def f2(string):
    r = []
    for c in range_char("a", "z"):
        if string.find(c) != -1: r.append(c)
    return len(r)

