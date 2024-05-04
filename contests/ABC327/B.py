b = int(input())

a = []
for i in range(1, 17):
    num = 1
    for j in range(i):
        num *= i
    a.append(num)

if b in a:
    print(a.index(b) + 1)
else:
    print(-1)