H = int(input())
p = 0
i = 0
d = 1
while p <= H:
    p += d
    d *= 2
    i += 1

print(i)