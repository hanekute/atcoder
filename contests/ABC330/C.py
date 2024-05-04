d = int(input())

xmax = int(d ** 0.5) + 1

ans = d

for i in range(xmax):
    c = i * i  - d
    if c >= 0:
        ans = min(ans, c)
    else:
        y_lower = int((c * -1) ** 0.5)
        y_upper = y_lower + 1
        ans = min(ans, abs(c + y_lower * y_lower), abs(c + y_upper * y_upper))

print(ans)

'''
√d < 1.5e6
xを固定した時のyは二択だから，全探索でもO(n^2)にはならない
'''