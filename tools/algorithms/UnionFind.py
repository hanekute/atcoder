'''
Union-Findの概要
できること
    2つのグループを1つにまとめる（Union）
    2つの要素が同じグループに属しているか判定する（Find）
構造
    Union = 片方の根からもう片方の根へ
    Find  = それぞれの根が等しければTrue
効率化の工夫
    １経路圧縮：根を調べるときに根に繋ぎなおす．実装が楽
    ２ランク：木の高さを保持しておいて，低い方を高い方につなげる
    片方やればO(logN)くらい，両方やればO(α(N))
できないこと
    集合の分割
'''
# ランクなし実装
# 親の配列
par = list()

# par初期化
def init(n):
    for i in range(n):
        par.append(i)
# 根を求める（経路圧縮もする）
def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
# 集合判定
def same(x, y):
    return root(x) == root(y)

# 集合の合体
def unite(x, y):
    x = root(x)
    y = root(y)
    if x ==y:
        return
    par[x] = y


# ランクあり実装
par = list()
rank = list()
# par初期化
def init(n):
    for i in range(n):
        par.append(i)
        rank.append(0)
# 根を求める（経路圧縮もする）
def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
# 集合判定
def same(x, y):
    return root(x) == root(y)

# 集合の合体
def unite(x, y):
    x = root(x)
    y = root(y)
    if x ==y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
