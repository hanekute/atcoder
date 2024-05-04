from itertools import permutations

U = 9*8*7*6*5*4*3*2

c = []
for _ in range(3):
    c += list(map(int, input().split()))

row_num = [
            (0, 3, 6), (0, 4), (0, 5, 7), 
            (1, 3), (1, 4, 6, 7), (1, 5), 
            (2, 3, 7), (2, 4), (2, 5, 6)]

count = 0
for x in permutations(range(9)):
    row_checked = [[] for _ in range(8)]
    flag = True
    for i in range(9):
        for j in row_num[x[i]]:
            row_checked[j].append(c[x[i]])
    for l in row_checked:
        if l[0] == l[1]:
            flag = False
            break
    if flag:
        count += 1

print(count / U)

# x: 何文字目を選ぶかの順番
# x[i]: i 番目に何文字目を選ぶか
# c[x[i]]: i番目に選ばれた数字
# 同じ数字が並ぶ2つを知った時点でアウト

'''
0~8の数字を並び替えた順列の1つをxとする
x[i]はi番目にどの位置を選ぶかを表し，c[x[i]]が実際の数
x[i]にある数字はタプルrow_num[x[i]]の各要素をインデックスとしてrow_checkedに格納
全部終わったら，row_checkedの各行の1文字目と2文字目を比較し，等しければアウト
'''
# 番号を付ける？
# 8つのリストを作って，1つずつ追加していく．2つ目が1つ目と同じならアウト
#    0      1      2      3      4      5      6      7
# (0,1,2)(3,4,5)(6,7,8)(0,3,6)(1,4,7)(2,5,8)(0,4,8)(2,4,6)