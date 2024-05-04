n = int(input())
s = sorted(input())

M = 10 ** n
i = 0
count = 0
while i * i < M:
    t = f'{i * i:0{n}}'    
    t = sorted(t)
    if s == t:
        count += 1
    i += 1
    
print(count)