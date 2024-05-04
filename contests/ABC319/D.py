n, m = map(int, input().split())
l = [int(x) for x in input().split()]

def f(width):
    w = l[0]
    line = 1
    for i in range(1, len(l)):
        w += l[i] + 1
        if w > width:
            line += 1
            w = l[i]
    return line

left = max(l)-1
right = sum(l) + n
while right - left > 1:
    mid = (left + right) // 2
    if f(mid) > m:
        left = mid
    else: 
        right = mid

else:
    print(right)