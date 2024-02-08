import random

def f1(string):
    l = string.split()
    random.shuffle(l)
    return " ".join(l)

def f2(string):
    k = 0
    l = string.split()
    for i in l:
        if len(i) % 2 == 0: k += 1
    return k

def f3(l):
    def keyFunc(string):
       if string == "белый": return 1
       elif string == "синий": return 2
       else: return 3
    return sorted(l, key=keyFunc)

num = input("Enter task number: ")
while True:
    if (num not in ["0","1","2"]): 
        num = input("Enter task number: ")
    else: break

if num == "2":
    l = []
    s = input()
    l.append(s)
    while s != "": 
        s = input()
        if (s != ""): l.append(s)
    print(f3(l))
    exit()


string = input("Enter input string: ")

if num == "0": print(f1(string))
elif num == "1": print(f2(string))