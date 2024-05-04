# 全部で2^10-2 = 1022通りしかない
# 全部リスト作って並べれば終わり

k = int(input())
from itertools import product # 多重ループをまとめられるやつ

l = list(i for i in range(10))[::-1] # 9,8,...,0

array = []

for pro in product((0, 1), repeat=10): # 0,1から選ぶのを10回繰り返す
    tmp = ''
    for i in range(10):
        if pro[i]:
            tmp += str(l[i])
    if tmp != '':
        array.append(int(tmp))

array.sort()
print(array[k])