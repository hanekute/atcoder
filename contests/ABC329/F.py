n, q = map(int, input().split())
c = [set()] + [{int(x)} for x in input().split()]

for i in range(q):
    a, b = map(int, input().split())
    if len(c[a]) > len(c[b]):
        c[a], c[b] = c[b], c[a]
    for x in c[a]:
        c[b].add(x)
    c[a].clear()
    print(len(c[b]))

'''
setで管理するのはOKだが，和集合を取るとTLE
必ず小さい方から大きい方に移すようにすると間に合う
'''