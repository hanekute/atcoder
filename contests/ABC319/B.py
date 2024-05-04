n = int(input())
s = ''
yakusu = list()
for i in range(1,10):
    if n % i == 0:
        yakusu.append(i)
        
for i in range(n+1):
    add = '-'
    for j in yakusu:
        x = n/j
        if i % x == 0:
            add = str(j)
            break
    s += add

print(s)