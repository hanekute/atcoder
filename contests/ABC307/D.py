n = int(input())
s = input()

a = []
t = ''
for i in range(n):
    if s[i] == '(':
        t += s[i]
        a.append(len(t)-1) # ここのindex勘違いしてた
    elif s[i] == ')':
        if a:
            t = t[:a[-1]]
            del a[-1]
        else:
            t += s[i]
    else:
        t += s[i]

print(t)