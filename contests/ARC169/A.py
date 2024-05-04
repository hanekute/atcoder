N = int(input())
A = [int(x) for x in input().split()]
P =[0] + [int(x) - 1 for x in input().split()]

depth = [0] * N

for i in range(1, N):
    depth[i] = depth[P[i]] + 1   

deepest = max(depth)

depthsum = [0] * (deepest + 1)
for i in range(N):
    depthsum[depth[i]] += A[i]
depthsum.reverse()

res = 0
for d in depthsum:
    if d != 0:
        res = d
        break

if res > 0:
    print('+')
elif res < 0:
    print('-')
else:
    print(0)

'''
Pに1がなかったら，A[0]の符号のまま
1を頂点とするツリーを作り，深さの配列も持つ
0を除いた一番深いやつの和の符号
'''