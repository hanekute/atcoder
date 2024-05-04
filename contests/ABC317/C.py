N,M=map(int,input().split())
# 座標(a, b)に長さを格納した二次元配列
# 必ず文字の通りに変数を用意する必要なし
E=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    E[a][b]=c
    E[b][a]=c

ans=0
used=[False]*(N+1)

# ansを更新する．返り値は無い
def dfs(v,s):
    global ans
    used[v]=True
    if s>ans: ans=s
    for i in range(1,N+1):
        # 未踏かつ道有りなら進む．
        if not used[i] and E[v][i]:
            dfs(i,s+E[v][i])
    used[v]=False

for i in range(1,N+1):
    dfs(i,0) # (現在地, 移動距離)

print(ans)
