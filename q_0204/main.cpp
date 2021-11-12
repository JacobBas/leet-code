#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <time.h>
using namespace std;

// this function is much quicker than the one below, but that is also given the
// fact that I'm not too sure how to efficiently use vectors as of this point
int primeSieveArray(int n)
{
    // handling the edge cases
    if (n < 2)
        return 0;

    // initializing a fully true array of values
    bool primes[n];
    std::fill_n(primes, n, 1);
    primes[0] = 0;
    primes[1] = 0;

    // looping through and testing the values
    for (int i = 2; i < sqrt(n); i++)
        if (primes[i] == true)
            for (int j = i * i; j < n; j += i)
                primes[j] = false;

    // summing up the trues to get the final value
    int count = 0;
    for (int i = 0; i < n; i++)
        count += primes[i];

    return count;
}

int primeSieveVector(int n)
{
    // handling the edge cases
    if (n < 2)
        return 0;

    // initializing a fully true array of values
    vector<bool> primes(n);
    std::fill(primes.begin(), primes.end(), true);
    primes[0] = 0;
    primes[1] = 0;

    // looping through and testing the values
    for (int i = 2; i < sqrt(n); i++)
        if (primes[i] == true)
            for (int j = i * i; j < n; j += i)
                primes[j] = false;

    // summing up the trues to get the final value
    return std::count(primes.begin(), primes.end(), true);
}

int main()
{
    int iter = 10000;
    time_t start, end, elapsed;

    time(&start);
    for (int i = 0; i < iter; i++)
    {
        primeSieveArray(i);
    }
    time(&end);
    elapsed = end - start;
    cout << elapsed << endl;

    time(&start);
    for (int i = 0; i < iter; i++)
    {
        primeSieveVector(i);
    }
    time(&end);
    elapsed = end - start;
    cout << elapsed << endl;

    return 0;
}