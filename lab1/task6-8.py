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

def f3(string):
    isNum = False
    min = -1
    cur = 0
    for c in string:
        if c in range_char("0","9") and not isNum:
            cur = int(c)
            isNum = True
        elif c in range_char("0","9") and isNum:
            cur = cur * 10 + int(c)
        elif c not in range_char("0","9") and isNum:
            isNum = False
            if min == -1: min = cur
            elif cur < min: min = cur
    if isNum and (cur < min or min == -1): min = cur
    return min

num = input("Enter task number: ")
while True:
    if (num not in ["0","1","2"]): 
        num = input("Enter task number: ")
    else: break

string = input("Enter input string: ")

if num == "0": print(f1(string))
elif num == "1": print(f2(string))
else: print(f3(string))