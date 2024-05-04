n, m = map(int, input().split())
a = [int(x) for x in input().split()]

ans = [0]*n

b = [a[0]]
for i in range(m-1):
    b.append(a[i+1]-a[i])

for i in b:
    for j in range(1,i+1):
        print(i-j)
