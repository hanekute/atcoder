N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

t = len(T)


first = [0] * N
count_first = [0] * (t + 1)

for i in range(N):
    s = S[i]
    x = 0
    k = 0
    for j in range(len(s)):
        if s[j] == T[k]:
            first[i] += 1
            k += 1
        if k == t:
            break
    count_first[k] += 1

rT = ''.join(list(reversed(T)))
rS = [''.join(list(reversed(s))) for s in S]

last = [0] * N
count_last = [0] * (t + 1)

for i in range(N):
    s = rS[i]
    x = 0
    k = 0
    for j in range(len(s)):
        if s[j] == rT[k]:
            last[i] += 1
            k += 1
        if k == t:
            break
    count_last[k] += 1

ans = 0
for i in range(t + 1):
    for j in range(t - i, t + 1):
        ans += count_first[i] * count_last[j]

print(ans)
'''
first[i]: S[i]が最初から何文字持っているか
last[i]:  S[i]が最後から何文字持っているか
count_first[i]: 最初からi文字持っている文字列の個数
count_last[i] : 最後からi文字持っている文字列の個数
'''