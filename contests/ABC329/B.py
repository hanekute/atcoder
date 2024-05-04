n = int(input())
a = [int(x) for x in input().split()]
a = set(a)
a.remove(max(a))
print(max(a))