s = list(input())
n = int(input())

for i in range(len(s)):
    if s[i] == '?':
        s[i] = '1'
        if int(''.join(s).replace('?', '0'), base=2) > n:
            s[i] = '0'

x = int(''.join(s), base=2)
if x <= n:
    print(x)
else:
    print(-1)

'''
大きい位から?を1に変えていく. nを超えない限り全部1に変えた結果が最大値

'''