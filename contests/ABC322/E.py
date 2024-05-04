# 動的計画法をかけるようになる必要がある
import numpy as np
n, k, p = map(int, input().split())
a = list()
c = list()
for i in range(n):
    t = [int(x) for x in input().split()]
    a.append(t[1:])
    c.append(t[0])

# a は二次n*k配列, a_tはその転置
a_t = np.array(a).T.tolist()

# 届かないならダメ
flag = True
for i in a_t:
    if sum(i) < p:
        flag = False
        break
if not flag:
    print(-1)
    
else:
    x=1