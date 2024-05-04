from collections import defaultdict
from bisect import bisect_left

w, h = map(int, input().split())
n = int(input())
pq = [tuple(map(int, input().split())) for _ in range(n)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

# 各イチゴの，切り分けられた(A+1)(B+1)グリッドにおける場所と個数を保持する辞書
counts = defaultdict(int)
for p, q in pq:
    x = bisect_left(a, p)
    y = bisect_left(b, q)
    counts[(x << 18) | y] += 1 # 2e5 < 2^18
    
M = max(counts.values())

if n < (A + 1) * (B + 1):
    m = 0
else:
    m = counts[0]
    for i in range(A + 1):
        for j in range(B + 1):
            m = min(m, counts[(i << 18) | j])
            
print(m, M)

'''
3秒までいける
    →O((A+1)(B+1))はループ内が単純ならギリセーフ
どのマスに何個イチゴが入るかを保持する辞書は簡単に作れる！defaultdictの利用
あとは二分探索で計算量削減
'''