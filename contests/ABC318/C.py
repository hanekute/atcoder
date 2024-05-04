n, d, p = map(int, input().split())
f = sorted([int(x) for x in input().split()])

taka = sum([i > p/d for i in f])
s0 = taka//d
s1 = s0+1
if s0 == 0: 
    p0 = sum(f)
else:
    p0 = sum(f[0:-s0*d])+p*s0
p1 = sum(f[0:-s1*d])+p*s1
print(min(p0, p1))