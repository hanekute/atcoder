n, t = input().split()
n = int(n)
s = [input() for _ in range(n)]

def check(a, b):
    if len(a) > len(b):
        return check(b, a)
    if len(a) < len(b) - 1:
        return False
    if a == b:
        return True
    else:
        i, j, e =0, 0, 0
        while i < len(a):
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                e += 1
                if e > 1:
                    return False
                if len(a) == len(b):
                    i += 1
                j += 1
        return True


ans = []
for i in range(n):
    if check(s[i], t):
        ans.append(i + 1)

print(len(ans))
print(' '.join(str(i) for i in ans))