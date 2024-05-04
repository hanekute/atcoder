n, m = map(int, input().split())
s = input()
t = input()

head = t[:n]
tail = t[-n:]
print(int((head != s))*2 + int((tail != s)))