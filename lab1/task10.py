def f(string):
    return len(string.split(" "))

l = []
s = input()
l.append(s)
while s: 
    s = input()
    if not s: l.append(s)
print(sorted(l, key=f))