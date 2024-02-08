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

