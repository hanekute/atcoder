import statistics

n = int(input())
a = [int(x) for x in input().split()]

m = statistics.mean(a) // 1
small = [x for x in a if x < m]
s = sum([m - x for x in small])
large = [x for x in a if x > m + 1]
l = sum([x - m - 1 for x in large])

print(int(max(s, l)))