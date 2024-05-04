n = int(input())

d = dict()

for i in range(n):
    s, c = map(int, input().split())
    r = 1
    while s % 2 == 0:
        r *= 2
        s /= 2
    try:
        d[s] += r * c
    except:
        d[s] = r * c

ans = 0
for v in d.values():
    ans += v.bit_count()

print(ans)
'''
s[i] = a * 2^r となるaで分類する
同じaのやつを合計してaで割った商を二進法で表した1の個数が最終的な匹数
'''