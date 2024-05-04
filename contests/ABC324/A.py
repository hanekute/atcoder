# リストの要素が全部同じならYes
# setにして要素数1か判定len(set(a))でよかった

N = int(input())
a = [int(x) for x in input().split()]
x = a[0]
f = True
for i in a:
    if i != x:
        f = False
        break
if f:
    print('Yes')
else:
    print('No')