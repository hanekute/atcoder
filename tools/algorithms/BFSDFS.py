from collections import deque

nodes = [[] for _ in range('node数')]
for i in range('edge数'):
    nodes['始点'].append('終点') # 集合なら.add

qu = deque() 
checked = [False] * 'node数'
qu.append('初期値')
checked['初期値'] = True

while qu:
    x = qu.popleft()
    for i in nodes[i]:
        # 処理
        if not checked[i]:
            qu.append(i)
            checked[i] = True



'''
# DFS
用意するもの
nodes[i] 頂点iから伸びる辺の先を持ったリストor 集合
stack スタック
checked 巡回済みかのチェック．
工程
stackに初期値をappend，checked[初期値]をTrueにする
stackが切れるまでループ:
'''
from collections import deque

nodes = [[] for _ in range('node数')]
for i in range('edge数'):
    nodes['始点'].append('終点') # 集合なら.add

stack = deque() 
checked = [False] * '数'
stack.append('初期値')
checked['初期値'] = True

while stack:
    x = stack.pop()
    for i in nodes[i]:
        # 処理
        if not checked[i]:
            stack.append(i)
            checked[i] = True
        
