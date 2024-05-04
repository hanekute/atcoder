x, y = map(int, input().split())
ans = 'No'
if -3 <= y - x <= 2:
    ans = 'Yes'
print(ans)