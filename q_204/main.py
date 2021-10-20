import math


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


if __name__ == '__main__':
    print(primeSieve(10000))
