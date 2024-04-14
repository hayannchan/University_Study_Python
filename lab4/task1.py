def findMax(fileName):
    f = open(fileName)
    s = f.readline().split()
    N = int(s[0])
    K = int(s[1])
    a=[]
    m1=-10**20
    m2=-10**20
    mx=-10**20
    for i in range(N):
        x=int(f.readline())
        a.append(x)
    for i in range(2*K, N):
        m1=max(m1, a[i-2*K])
        m2=max(m2, m1+a[i-K])
        mx=max(mx, m2+a[i])
    return mx

print(findMax("test.txt"))
print(findMax("27-166a.txt"))
print(findMax("27-166b.txt"))