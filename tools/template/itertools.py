import itertools

# itertools関係

n = int()
p, q = list(), list()
r = int()

# 文字列なら文字列になる．intならタプル？

# p, qから1個ずつ選んだタプルの全パターン
itertools.product(p, q)
itertools.product(p, repeat=n)

# pからr個選ぶ順列，組み合わせ，重複あり組み合わせ
itertools.permutations(p, r)
itertools.combinations(p, r)
itertools.combinations_with_replacement(p, r)

# リストの累積和
itertools.accumulate(p)

# 参考: https://docs.python.org/ja/3/library/itertools.html