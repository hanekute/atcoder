h, w = map(int, input().split())
c = [['.'] + list(input()) + ['.'] for _ in range(h)]
n = min(h, w)
c = [['.']*(w+2)] + c + [['.']*(w+2)]
s = [0]*(n+1)

for y in range(1,h+1):
    for x in range(1, w+1):
        if c[y][x] == '#':
            batsu = True
            for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                ny, nx = y+dy, x+dx
                if c[ny][nx] == '.':
                    batsu = False
                    break
            if batsu:
                size = 1
                flag = True
                while flag:
                    for dy, dx in [(-size-1, -size-1), (-size-1, size+1), (size+1, -size-1), (size+1, size+1)]:
                        ny, nx = y+dy, x+dx
                        if c[ny][nx] == '.':
                            flag = False
                    size += 1*flag
                s[size] += 1
print(' '.join(str(i) for i in s[1:]))