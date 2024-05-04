money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    print("pattern {}: ".format(i), end="")
    for j in range(n):
        if ((i >> j) & 1):
            bag.append(item[j][0])
    print(bag)

'''
O(2^n)だからn=30くらいまでは2sでいける？
n個の組み合わせ2^n個
2^nの中のループ
    各桁でループ
        各桁目が1なら:
            処理
'''