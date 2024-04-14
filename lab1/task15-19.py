def func1(l, i):
    if l[i] == max(l): return True
    else: return False

def func2(l, i):
    if i != 0 and l[i-1] < l[i]: return False
    if i != len(l) - 1 and l[i+1] < l[i]: return False
    return True

def func3(l):
    first = l[0]
    for i in range(1,len(l)):
        l[i-1] = l[i]
    l[len(l)-1] = first
    return l

def func4(l):
    l1 = []
    l2 = []
    for i in range(0,len(l)):
        if i % 2 == 0: l1.append(l[i])
        else: l2.append(l[i])
    return l1 + l2

def func5(l):
    l1 = []
    l2 = []
    for i in l:
        if i not in l1: 
            l1.append(i)
            l2.append(1)
        else:
            l2[l1.index(i)] += 1
    return [l1, l2]

num = input("Enter task number: ")
while True:
    if (num not in ["0","1","2","3","4"]): 
        num = input("Enter task number: ")
    else: break

if num in ["2","3","4"]:
    l = []
    s = input()
    l.append(int(s))
    while s != "": 
        s = input()
        if (s != ""): l.append(int(s))
    if num == "2": print(func3(l))
    elif num == "3": print(func4(l))
    else: print(func5(l))
    exit()
elif num in ["0","1"]:
    l = []
    s = input()
    l.append(int(s))
    while s != "": 
        s = input()
        if (s != ""): l.append(int(s))
    i = input()
    if num == "0": print(func1(l, int(i)))
    else: print(func2(l, int(i)))