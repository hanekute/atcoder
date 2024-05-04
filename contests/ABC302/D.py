n, m, d = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort(reverse=True)
b.sort(reverse=True)

i = 0
j = 0


vmax = -1
while True:
    aa = a[i]
    bb = b[j]
    if abs(aa - bb) <= d:
        vmax = aa + bb
        break
    if aa > bb:
        i += 1
    else:
        j += 1
    if i == n or j == m:
        break

print(vmax)