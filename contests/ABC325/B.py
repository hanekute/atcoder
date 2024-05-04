n = int(input())
w = []
x = []
a = [ list(map(int,input().split(" "))) for _ in range(n)]
for i in range(n):
    w.append(a[i][0])
    x.append(a[i][1])
    
sanka = [0]*24
for j in range(n):
    for k in range(x[j]+9, x[j]+18):
        sanka[k%24] += w[j]

print(max(sanka))