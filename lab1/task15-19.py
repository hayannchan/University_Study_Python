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

