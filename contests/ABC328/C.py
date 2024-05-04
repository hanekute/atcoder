import bisect

n, q = map(int, input().split())
s = input()

renzoku = []
for i in range(n - 1):
    if s[i] == s[i + 1]:
        renzoku.append(i)
        
for i in range(q):
    l, r = map(int, input().split())
    print(bisect.bisect_left(renzoku, r - 1) - bisect.bisect_left(renzoku, l - 1))

'''
11文字
mississippi
i = 2, 5, 8で隣り合う
renzoku = [2, 5, 8]
tonari(1) = 0
tonari(2) = 0
tonari(3) = 1
3,9 => s[2]からs[8]ssissip
bisectleft
'''