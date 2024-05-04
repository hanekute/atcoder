from collections import defaultdict
n = int(input())
s = input()

counts = defaultdict(int)

x = 1
counts[s[0]] = 1
for i in range(1, n):
    if s[i] == s[i - 1]:
        x += 1
        counts[s[i]] = max(counts[s[i]], x)
    else:
        x = 1
        counts[s[i]] = max(counts[s[i]], x)

ans = sum(counts.values())
print(ans)