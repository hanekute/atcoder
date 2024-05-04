# 全部で2^10-2 = 1022通りしかない
# 全部リスト作って並べれば終わり

# 1~1023を二進法→文字列→9~0を割り当てる->整数に戻してソートという案
k = int(input())
l = list(range(2,1024))
l_bi = [f'{i:10b}' for i in l]

l_kazu = list()

for b in l_bi:
    kazu_str = ''
    for i in range(10):
        if b[i] == '1':
            kazu_str += str(9-i)
    l_kazu.append(kazu_str)

ans = [int(i) for i in l_kazu]
ans = sorted(ans)
print(ans[k-1])