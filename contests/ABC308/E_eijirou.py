n = int(input())
a = list(map(int, input().split()))
s = input()

counts = [[0] * 8 for _ in range(2)]
ans = 0

# i桁目: iを含むとき1
def mex(x):
    if not x & 1:
        return 0
    elif not (x >> 1) & 1:
        return 1
    elif not (x >> 2) & 1:
        return 2
    else:
        return 3

for i in range(n):
    if s[i] == 'M':
        counts[0][1 << a[i]] += 1
    elif s[i] == 'E':
        for j in range(8):
            # ここ分かってない
            counts[1][j | (1 << a[i])] += counts[0][j]
    else:
        for j in range(8):
            ans += mex(j | (1 << a[i])) * counts[1][j]

print(ans)

'''
eijirouの解答
mexの計算はビットで行う
countsは2行8列

Xが出てきたら，その前にどんなMとどんなEがあるかで
'''