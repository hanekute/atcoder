from itertools import accumulate
n, m, p = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a = sorted(a, reverse=True)
b = sorted(b)
b_sum = list(accumulate(b))

ans = 0
j = 0
for i in range(n):
    while j < m and a[i] + b[j] < p:
        j += 1
    if j == 0:
        ans += p * m
    else:
        ans += a[i] * j + b_sum[j - 1] + p * (m - j)

print(ans)
'''
aは大きい順，bは小さい順に並べる
bの小さい順の累積和をb_sumに用意

aをソートせず，各a[i]について二分探索でjを求めるという方針もある
'''