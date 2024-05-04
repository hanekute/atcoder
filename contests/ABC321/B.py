n, x = map(int, input().split())

a = [int(i) for i in input().split()]
score = sorted(a)
s = sum(score[1:-1])
left = x-s
ans = 0
if left <= score[0]: ans = 0
elif left <= score[-1]: ans = left
else: ans = -1
print(ans)