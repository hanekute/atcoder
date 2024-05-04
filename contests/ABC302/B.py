h, w = map(int, input().split())
s = [input() for _ in range(h)]

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(h):
    for j in range(w):
        if s[i][j] == 's':
            for di, dj in directions:
                if 0 <= i + 4 * di < h and 0 <= j + 4 * dj < w:
                    if s[i + di][j + dj] == 'n' and s[i + 2 * di][j + 2 * dj] == 'u' and s[i + 3 * di][j + 3 * dj] == 'k' and s[i + 4 * di][j + 4 * dj] == 'e':
                        i += 1
                        j += 1
                        print(f'{i} {j} \n{i + di} {j + dj} \n{i + 2 * di} {j + 2 * dj} \n{i + 3 * di} {j + 3 * dj} \n{i + 4 * di} {j + 4 * dj}')
                        exit()