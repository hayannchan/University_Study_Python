def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def sort1(l):
    def keyFunc(string):
        maxChar = ""
        maxCount = 0
        for c in string:
            if maxCount < l.count(c): 
                maxChar = c
                maxCount = l.count(c)
        if maxChar in range_char("A", "z"): return (maxCount / len(string)) - (1 / 26)
        elif maxChar in range_char("А", "я"): return (maxCount / len(string)) - (1 / 33)
        else: return maxCount / len(string)

freq = {
    "a": 0.0817,
    "b": 0.0149,
    "c": 0.0278,
    "d": 0.0425,
    "e": 0.1270,
    "f": 0.0223,
    "g": 0.0202,
    "h": 0.0609,
    "i": 0.0697,
    "j": 0.0015,
    "k": 0.0077,
    "l": 0.0403,
    "m": 0.0241,
    "n": 0.0675,
    "o": 0.0751,
    "p": 0.0193,
    "q": 0.0010,
    "r": 0.0599,
    "s": 0.0633,
    "t": 0.0906,
    "u": 0.0276,
    "v": 0.0098,
    "w": 0.0236,
    "x": 0.0015,
    "y": 0.0197,
    "z": 0.0007
}

def sort2(l):
    def keyFunc(string):
        string = string.lower()
        maxChar = string[0]
        maxCount = 0
        for c in string:
            if maxCount < string.count(c): 
                maxChar = c
                maxCount = string.count(c)
        r = freq[maxChar]
        print(r)
        return (maxCount / len(string) - r) ** 2
    
    return sorted(l, key=keyFunc)

