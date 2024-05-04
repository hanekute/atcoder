n = int(input())
a = list(map(int, input().split()))
s = input()

def mex(x, y, z):
    for i in range(4):
        if i not in [x, y, z]:
            return i
    
ans = 0

count_m = [[0] * 3 for _ in range(n)]
count_x = [[0] * 3 for _ in range(n)]

for i in range(n):
    if i > 0:
        # count_m[i] = count_m[i - 1] では，count_m[i - 1]まで変更される
        count_m[i] = [u + v for u, v in zip(count_m[i], count_m[i - 1])]
    if s[i] == 'M':
        count_m[i][a[i]] += 1

for i in reversed(range(n)):
    if i < n - 1:
        count_x[i] = [u + v for u, v in zip(count_x[i], count_x[i + 1])]
        # count_x[i] = count_x[i + 1]
    if s[i] == 'X':
        count_x[i][a[i]] += 1

for i in range(n):
    if s[i] != 'E':
        continue
    for j in range(3):
        for k in range(3):
            ans += mex(j, k, a[i]) * count_m[i][j] * count_x[i][k]

print(ans)

'''

Eの前のMの数
count_m: i文字目までのMの数(aの値別に集計)
count_x: i文字目からのXの数(aの値別に集計)

Pythonは値渡しだが，ここの代入は注意が必要
'''