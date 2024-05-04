N = int(input())

def div_two(n):
    x = 2
    ans = 0
    while x <= n:
        ans += 1
        x *= 2
    return ans

k = div_two(N)
ans = N * k + 2 * (N - 2 ** k)

print(ans)