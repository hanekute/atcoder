N = int(input())
A = [int(x) for x in input().split()]

min_ = 0
sum_ = 0
for i in A:
    sum_ += i
    if sum_ < min_:
        min_ = sum_

print(sum_ - min_)