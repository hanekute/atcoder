from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

def count_true(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if element == True:
                count += 1
    return count

for I in range(H):
    for J in range(W):
        if S[I][J] == "#":
            if I > 0:
                if S[I-1][J] == ".":
                    S[I-1][J] = "o"
            if J > 0:
                if S[I][J-1] == ".":
                    S[I][J-1] = "o"
            if J < W - 1:
                if S[I][J+1] == ".":
                    S[I][J+1] = "o"
            if I < H - 1:
                if S[I+1][J] == ".":
                    S[I+1][J] = "o"

ans = 0
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            stack = deque()
            checked = [[False] * W for _ in range(H)]
            stack.append((i, j))
            checked[i][j] = True
            
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    if 0 <= x + dx < H and 0 <= y + dy < W:
                        if S[x + dx][y + dy] == "." and not checked[x + dx][y + dy]:
                            stack.append((x + dx, y + dy))
                            checked[x + dx][y + dy] = True
                        elif S[x + dx][y + dy] == "o" and not checked[x + dx][y + dy]:
                            checked[x + dx][y + dy] = True
            res = count_true(checked)
            if ans < res:
                ans = res

print(ans)