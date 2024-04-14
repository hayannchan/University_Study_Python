n = int(input())
dictionary = {}
for _ in range(n):
    s = input().split()
    dictionary[s[0]] = s[1]
    dictionary[s[1]] = s[0]
s = input()
print(dictionary[s])