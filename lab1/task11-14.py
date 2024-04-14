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
    return sorted(l, key=keyFunc)

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
        maxChar = string[0] #значение первого символа в строке
        maxCount = 0
        for c in string:
            if maxCount < string.count(c): #текущее макс колво меньше колва символов с то новый самый часто встречаемый это с
                maxChar = c
                maxCount = string.count(c)
        r = freq[maxChar]
        return (maxCount / len(string) - r) ** 2
    return sorted(l, key=keyFunc)

def sort3(l):
    def keyFunc(string):
        k = 0
        for i in range(1,len(string)):
            if ((string[i-1] in ["a", "e", "y", "u", "i", "o"]) and (string[i] not in ["a", "e", "y", "u", "i", "o"])) or ((string[i-1] not in ["a", "e", "y", "u", "i", "o"]) and (string[i] in ["a", "e", "y", "u", "i", "o"])):
                k += 1
        return k
    return sorted(l, key=keyFunc)

def sort4(l):
    n = len(l)
    lines = l
    symbols_freqs = {}

    for line in lines:
        for symb in line:
            if symb in symbols_freqs:
                symbols_freqs[symb] += 1
            else:
                symbols_freqs[symb] = 1
    freqs = list(symbols_freqs.values())
    symbols = list(symbols_freqs.keys())
    mx = [max(freqs) / n, symbols[freqs.index(max(freqs))]]
    # print(mx)

    for i in range(n - 1):
        for j in range(i + 1, n):
            # sqrt((xi - x)^2) = abs(xi - x)
            if abs(lines[i].count(mx[1]) - mx[0]) > abs(lines[j].count(mx[1]) - mx[0]):
                lines[i], lines[j] = lines[j], lines[i]
    return lines

num = input("Enter task number: ")
while True:
    if (num not in ["0","1","2","3"]): 
        num = input("Enter task number: ")
    else: break

l = []
s = input()
l.append(s)
while s != "": 
    s = input()
    if (s != ""): l.append(s)

if num == "0": print(sort1(l))
elif num == "1": print(sort2(l))
elif num == "2": print(sort3(l))
else: print(sort4(l))