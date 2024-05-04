from collections import deque
N = int(input())
A = [int(x) for x in input().split()]

def merge(a, b):
    0

numbers = deque()
leng = 0
for i in range(N):
    numbers.append(A[i])
    leng += 1
    while leng > 1:
        a = numbers.pop()
        b = numbers.pop()
        if a == b:
            numbers.append(a + 1)
            leng -= 1
        else:
            numbers.append(b)
            numbers.append(a)
            break

print(len(numbers))
