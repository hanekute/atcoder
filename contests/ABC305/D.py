import bisect
n = int(input())
a = [int(x) for x in input().split()]
q = int(input())

# 0~t分の間に寝ていた分数を返すf(t)
# a[i]分までに寝ていた分数fa(i)

fa = [0]*n
for i in range(1,n):
    if i % 2 == 0:
        fa[i] = fa[i - 1] + a[i] - a[i - 1]
    else:
        fa[i] = fa[i - 1]

def f(t):
    # a[j]<= t < a[j+1]となるjを求める
    j = bisect.bisect_right(a, t) - 1
    if j % 2 != 0:
        return int(fa[j] + (t - a[j])*(fa[j + 1] - fa[j]) / (a[j + 1] - a[j]))
    else:
        return fa[j]

for i in range(q):
    l, r = map(int, input().split())
    print(f(r) - f(l))