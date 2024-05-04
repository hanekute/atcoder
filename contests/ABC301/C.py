from collections import defaultdict
s = input()
t = input()

scount = defaultdict(int)
tcount = defaultdict(int)

for c in s:
    scount[c] += 1
for c in t:
    tcount[c] += 1

for c in 'atcoder':
    m = max(scount[c], tcount[c])
    if scount['@'] < m - scount[c] or tcount['@'] < m - tcount[c]:
        print('No')
        exit()
    scount['@'] -= m - scount[c]
    scount[c] = m
    tcount['@'] -= m - tcount[c]
    tcount[c] = m

if scount == tcount:
    print('Yes')
else:
    print('No')