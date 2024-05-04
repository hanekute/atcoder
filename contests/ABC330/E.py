N, Q = map(int, input().split())
A = [int(x) for x in input().split()]

counter = [0] * (N + 1)
for a in A:
    if a > N:
        continue
    counter[a] += 1

mexs = set()
for i in range(N + 1):
    if counter[i] == 0:
        mexs.add(i)

for _ in range(Q):
    i, x = map(int, input().split())
    i -= 1
    counter[A[i]] -= 1
    if counter[A[i]] == 0:
        mexs.add(A[i])
    if x <= N:
        counter[x] += 1
        if x in mexs:
            mexs.remove(x)
    A[i] = x
    print(min(mexs))

'''
N個の数列のmexはN以下
含まれない数のsetを用意する
'''