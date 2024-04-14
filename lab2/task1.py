s = input().split()
N, M = int(s[0]), int(s[1])
A = set()
for _ in range(N):
    A.add(input())
B = set()
for _ in range(M):
    B.add(input())
common = sorted(list(A.intersection(B)), key=int)
print(str(len(common))+"\n"+" ".join(common))
AnyaOnly = sorted(list(A.difference(B)), key=int)
print(str(len(AnyaOnly))+"\n"+" ".join(AnyaOnly))
BoryaOnly = sorted(list(B.difference(A)), key=int)
print(str(len(BoryaOnly))+"\n"+" ".join(BoryaOnly))