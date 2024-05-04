n = int(input())
s = input()
q = int(input())

status = []
for i in range(n):
    status.append([0, s[i]])

fill = []

for i in range(q):
    t, x, c = input().split()
    t, x = int(t), int(x)
    if t == 1:
        status[x - 1] = [i, c]
    else:
        fill = [i, t]

for time, c in status:
    if not fill or time >= fill[0]:
        print(c, end='')
    elif fill[1] == 2:
        print(c.lower(), end='')
    else:
        print(c.upper(), end='')

print()