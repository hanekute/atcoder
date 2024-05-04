n, m = map(int, input().split())
a = [int(x) for x in input().split()]

votes = [0]*(1 + n)
max_votes = 0
winner = n
for i in range(m):
    v = a[i]
    votes[v] += 1
    if votes[v] == max_votes:
        winner = min(v, winner)
        max_votes = votes[v]
    elif votes[v] > max_votes:
        winner = v
        max_votes = votes[v]
    print(winner)

# 最大得票数と暫定当選者を別で用意