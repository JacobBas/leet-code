#include <iostream>
#include <math.h>
using namespace std;

int primeSieve(int n)
{
    if (n < 2)
        return 0;

    bool primes[n];
    std::fill_n(primes, n, 1);
    primes[0] = 0;
    primes[1] = 0;

    for (int i = 2; i < sqrt(n); i++)
        if (primes[i] == true)
            for (int j = i * i; j < n; j += i)
                primes[j] = false;

    int count = 0;
    for (int i = 0; i < n; i++)
        count += primes[i];

    return count;
}

long factorial(int n)
{
    int mod = 1000000007;
    if (n < 2)
        return 1;

    long x = 1;
    for (int i = 1; i <= n; i++)
    {
        x *= i;
        if (x >= mod)
            x %= mod;
    }

    return x;
}

int numPrimeArrangements(int n)
{
    int mod = 1000000007;
    int s_prime, s_other;
    s_prime = primeSieve(n + 1);
    s_other = n - s_prime;

    return (factorial(s_prime) * factorial(s_other)) % mod;
}

int main()
{
    int n = 100;
    cout << numPrimeArrangements(n) << endl;
    return 0;
}