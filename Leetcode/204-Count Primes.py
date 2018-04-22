def countPrimes(n):
    if n <= 2:
        return 0

    primes = [True] * n
    # 0 and 1 don't count as primes
    primes[0] = primes[1] = False

    for i in range(2,n):
        if primes[i]:
            # List slcing with increment. Start at i*i instead i for optimization
            primes[i*i: n: i] = [False] * len(primes[i*i: n: i])

    return sum(primes)

print(countPrimes(7))
