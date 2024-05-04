import math
import collections

# 最大公約数GCD, 最小公倍数LCM
x, y, z = 6, 8, 10
l = [x, y, z]

math.gcd(x, y)
math.lcm(x, y)

math.gcd(x, y, z)
math.lcm(x, y, z)

math.gcd(*l)
math.lcm(*l)

# 約数列挙
def make_divisors(n: int) -> list:
    return_list = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            return_list.append(i)
            if i != n // i:
                return_list.append(n//i)
    return return_list

# 素因数分解 O(√n) 素数のリストを返す．3以上は全奇数を調べる
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

# 素数と個数の辞書
c = collections.Counter(prime_factorize(840))
print(c)
# Counter({2: 3, 3: 1, 5: 1, 7: 1})

# n以下の素数を列挙した配列を作る（エラトステネスの篩）O(N log log N)
def Eratosthenes(N):
    isprime = [True] * (N+1)

    isprime[0], isprime[1] = False, False

    for p in range(2, N+1):
        if not isprime[p]:
            continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p
    
    primes = []
    
    for i in range(N + 1):
        if isprime[i]:
            primes.append(i)
    return primes
