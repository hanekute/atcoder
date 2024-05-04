n, m, h, k = map(int, input().split())
s = input()

item = set(tuple(map(int, input().split())) for _ in range(m))

ans = 'Yes'
x, y = 0, 0
for i in range(n):
    if s[i] == 'R':
        x += 1
    elif s[i] == 'L':
        x -= 1
    elif s[i] == 'U':
        y += 1
    else:
        y -= 1
    h -= 1
    if h < 0:
        ans = 'No'
        break
    if (x, y) in item and h < k:
        h = k
        item.remove((x, y))

print(ans)