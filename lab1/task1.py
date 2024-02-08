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

