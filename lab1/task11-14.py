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
