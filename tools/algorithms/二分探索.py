import bisect
# m以上は全て条件を満たす最小のmを求める→イコールなら右を寄せ，右を返す でもbisect.left()
# m以下は全て条件を満たす最大のmを求める→イコールなら左を寄せ，左を返す でもbisect.right()

x = 0
# ソートされたlistの中にxを入れたときのxのindexを返す
# right:等しい要素があったらその次に入れる
bisect.bisect_right(list, x)
# left :等しい要素があったらその前に入れる
bisect.bisect_left(list, x)



# 手書きも
# 0~nで条件を満たす最小の値mを求める
# m 以上なら全て条件満たす→イコールなら右を寄せ，右を返す
n = 0
joken = []
def bs_min(t):
    left = 0
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if joken[mid]: 
            right = mid
        else: 
            left = mid
    return right

# 0~nで条件を満たす最大の値mを求める
def bs_max(t):
    left = 0
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if mid <= t:
            left = mid
        else: 
            right = mid
    return left