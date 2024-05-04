m = int(input())
s = [input() for _ in range(3)]
# 最長でも3周 = 3m-1秒 <= 299 299^3 <= 3e7

for i in range(3):
    s[i] += s[i] + s[i]

res = 300
for i in range(len(s[0])):
    for j in range(len(s[0])):
        if j == i:
            continue
        for k in range(len(s[0])):
            if k == i or k == j:
                continue
            if s[0][i] == s[1][j] == s[2][k]:
                res = min(res, max(i, j, k))

print(res if res < 300 else -1)
