n, q = map(int, input().split())
# 工夫なし．孤立の数を別で用意したことくらい？
nodes = [set() for _ in range(n + 1)]
solo = n

for i in range(q):
    qu = input().split()
    if qu[0] == '1':
        u, v = int(qu[1]), int(qu[2])
        if len(nodes[u]) == 0:
            solo -= 1
        if len(nodes[v]) == 0:
            solo -= 1
        nodes[u].add(v)
        nodes[v].add(u)
    else:
        u = int(qu[1])
        if len(nodes[u]) == 0:
            print(solo)    
            continue
        for v in nodes[u]:
            if len(nodes[v]) == 0:
                continue
            nodes[v].remove(u)
            if len(nodes[v]) == 0:
                solo += 1
        nodes[u].clear()
        solo += 1
    print(solo)

'''
listとsetの計算量の違い
            追加       削除
list        O(1)       O(N)
set       O(logN)    O(logN)
'''