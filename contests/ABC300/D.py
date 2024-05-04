n = int(input())

MAXP = 288675
isprime = [True] * (MAXP+1)
isprime[0], isprime[1] = False, False

for p in range(2, MAXP):
    if not isprime[p]:
        continue

    q = p * 2
    while q <= MAXP:
        isprime[q] = False
        q += p

primes = []

for i in range(len(isprime)):
    if isprime[i]:
        primes.append(i)

le = len(primes)
res = 0
for i in range(le):
    if primes[i] * primes[i] * primes[i + 1] * primes[i + 2] * primes[i + 2] > n:
        break
    for j in range(i + 1, le):
        if primes[i] * primes[i] * primes[j] * primes[j + 1] * primes[j + 1] > n:
            break
        for k in range(j + 1, le):
            if primes[i] * primes[i] * primes[j] * primes[k] * primes[k] > n:
                break
            res += 1

print(res)