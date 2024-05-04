n = list(input())
ans = 'Yes'
if len(n) == 1: print(ans)
else:
    for i in range(len(n)-1):
        if n[i] <= n[i+1]:
            ans = 'No'
            break
    print(ans)