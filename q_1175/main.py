import math

mod = 1000000007


def primeSieve(n: int) -> int:
    if n < 2:
        return 0

    primes = [1 for _ in range(n)]
    primes[0], primes[1] = 0, 0

    i = 2
    while i < math.sqrt(n):
        if primes[i] == 1:
            j = i * i
            while j < n:
                primes[j] = 0
                j += i
        i += 1

    return sum(primes)


def factorial(n: int) -> int:
    if n < 2:
        return 1

    x = 1
    for i in range(1, n + 1):
        x *= i
        if x >= mod:
            x %= mod
    return x


def numPrimeArrangements(n: int) -> int:
    s_prime = primeSieve(n+1)
    s_other = n - s_prime

    return (factorial(s_prime) * factorial(s_other)) % mod


if __name__ == '__main__':
    print(numPrimeArrangements(100))
