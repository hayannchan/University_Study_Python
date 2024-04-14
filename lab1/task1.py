def is_prime(num):
    f = True
    for i in range(2,num):
        if num % i == 0: 
            f = False
            break
    return f

def func1(num):
    r = 1
    for i in range(2,num + 1):
        if num % i == 0 and is_prime(i): r = i
    return r

def func2(num):
    r = 1
    while num:
        if (num % 10) % 5 != 0:
            r *= num % 10
        num = int(num / 10)
    return r

def func3(num):
    r1 = 1
    for i in range(2,num + 1):
        if num % i == 0 and not is_prime(i) and i % 2 == 1: r1 = i
    r2 = 1
    while num:
        r2 *= num % 10
        num = int(num / 10)
    l1 = []
    for i in range(1, r1 + 1):
        if r1 % i == 0: l1.append(i)
    l2 = []
    for i in range(1, r2 + 1):
        if r2 % i == 0: l2.append(i)
    r = 1
    for i in l1:
        if i in l2 and i > r: r = i
    return r