# 整数の入力
N = int(input())
N, M = map(int, input().split())

# 横に並んだ整数 
A = [int(x) for x in input().split()]

# 縦に並んだ整数
A = [int(input()) for _ in range(N)]

# 整数の2次元配列
A = [list(map(int,input().split(" "))) for _ in range(N)]

# 縦の列を1つの配列として
X, Y  = [], []
A_ = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    X.append(A_[i][0])
    Y.append(A_[i][1])

# 縦の列をタプルのリストとして
XY = [tuple(map(int, input().split())) for _ in range(N)]

# 文字列の入力
S = input()
S, T = input().split()
S = [input() for _ in range(N)]