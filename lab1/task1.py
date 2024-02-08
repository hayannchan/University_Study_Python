def isPrime(num):
    f = True
    for i in range(2,num):
        if num % i == 0: 
            f = False
            break
    return f

def func1(num):
    r = 1
    for i in range(2,num + 1):
        if num % i == 0 and isPrime(i): r = i
    return r

def func2(num):
    r = 0
    while num:
        if (num % 10) % 5 != 0:
            r *= num % 10
        num = int(num / 10)
    return r

