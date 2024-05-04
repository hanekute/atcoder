s = input()
ans = ''
for x in s:
    if x == '.':
        ans = ''
    else:
        ans += x

print(ans)