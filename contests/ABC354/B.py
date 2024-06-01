N = int(input())
S, C  = [], []
for i in range(N):
    s, c = input().split()
    c = int(c)
    S.append(s)
    C.append(c)

T = sum(C)

win = T % N
S.sort()

print(S[win])