h, w = map(int, input().split())
a = [input() for _ in range(h)]
b = [input() for _ in range(h)]
b = b + b
b = [b[i] + b[i] for i in range(len(b))]

for i in range(h):
    for j in range(w):
        flag = True
        for k in range(h):
            if a[k] != b[k + i][j:j + w]:
                flag = False
                break
        if flag:
            print('Yes')
            exit()
        
print('No')