n = int(input())
t = set()
for _ in range(n):
    s = input()
    t.add(min(s, s[::-1]))
print(len(t))