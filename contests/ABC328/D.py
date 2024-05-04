from collections import deque

s = input()

a_keep = 0
ab_keep = 0

ans = ''

stack = deque()
lenstack = 0

for i in range(len(s)):
    if lenstack < 2:
        stack.append(s[i])
        lenstack += 1
    else:
        if s[i] == 'C':
            if stack[-1] == 'B' and stack[-2] == 'A':
                x = stack.pop()
                x = stack.pop()
                lenstack -= 2
            else:
                stack.append(s[i])
                lenstack += 1
        else:
            stack.append(s[i])
            lenstack += 1

print(''.join(i for i in stack))

'''
どんどんstackに入れていき，Cを見つけたら末尾から見てABCになったらABを削除．
'''