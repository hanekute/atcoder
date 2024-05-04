n = int(input())
a = []
b = []
c = []
d = []
l = [ list(map(int,input().split(" "))) for _ in range(n)]
for i in range(n):
    a.append(l[i][0])
    b.append(l[i][1])
    c.append(l[i][2])
    d.append(l[i][3])
    
anslist = [[0] * 100 for i in range(100)]

for i in range(n):
    for j in range(a[i], b[i]):
        for k in range(c[i], d[i]):
            anslist[j][k] = 1

total = 0
for i in anslist:
    val = sum(i)
    total += val

print(total)