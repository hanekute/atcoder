# 「10^9+7で割った余りを求めよ」問題
# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a
MOD = 10**9 + 7

a, b = int(), int()
# 加減乗は普通にできる（引き算で正の余りが出るのはPythonならでは）
a * b % MOD * a % MOD

# 割り算 「逆元をかける」
# 整数aのmにおける逆元を求める関数O(log m)
def modinv(a, m): 
    b = m
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u

# a÷bのmod m
a % MOD * modinv(b, MOD) % MOD

# 累乗a^nをO(log n)で行う
# 二分累乗法
def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1: # 1ビット目が1
            res = res * a % mod
        a = a * a % mod
        n >>= 1 # 右シフト
    return res

# 二項係数nCr
