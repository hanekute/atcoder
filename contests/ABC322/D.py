p11 = [input() for _ in range(4)]
p21 = [input() for _ in range(4)]
p31 = [input() for _ in range(4)]

# 全通り試す？
def kaiten(p):
    newp = p
    for i in range(4):
        for j in range(4):
            newp[i][j] = p[3-j][i]
    return newp
# 1個目の位置と向き→2個目の位置と向き→3個目の位置と向きで全探索
p12 = kaiten(p11)
p13 = kaiten(p12)
p14 = kaiten(p13)
p22 = kaiten(p21)
p23 = kaiten(p22)
p24 = kaiten(p23)
p32 = kaiten(p31)
p33 = kaiten(p32)
p34 = kaiten(p33)
p1 = [p11, p12, p13, p14]
p2 = [p21, p22, p23, p24]
p3 = [p31, p32, p33, p34]