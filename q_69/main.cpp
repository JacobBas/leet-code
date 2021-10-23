#include <iostream>
#include <assert.h>
#include <math.h>
using namespace std;

int sqrt(int x)
{
    if (x < 2)
        return x;

    int l = 0, r = x;
    long mid;
    while (l <= r)
    {
        mid = (l + r) / 2;

        if ((mid * mid) <= x && x < (mid + 1) * (mid + 1))
            break;

        if (x < (mid * mid))
            r = mid;
        else
            l = mid;
    }

    return mid;
}

int main()
{
    int input, output;

    input = 0;
    output = std::sqrt(input);
    std::cout << "Begin test 1 ... ";
    assert(sqrt(input) == output);
    std::cout << "Success!" << endl;

    input = 1;
    output = std::sqrt(input);
    std::cout << "Begin test 2 ... ";
    assert(sqrt(input) == output);
    std::cout << "Success!" << endl;

    input = 4;
    output = std::sqrt(input);
    std::cout << "Begin test 3 ... ";
    assert(sqrt(input) == output);
    std::cout << "Success!" << endl;

    input = 8;
    output = std::sqrt(input);
    std::cout << "Begin test 4 ... ";
    assert(sqrt(input) == output);
    std::cout << "Success!" << endl;

    input = 15;
    output = std::sqrt(input);
    std::cout << "Begin test 5 ... ";
    assert(sqrt(input) == output);
    std::cout << "Success!" << endl;

    input = 45;
    output = std::sqrt(input);
    std::cout << "Begin test 6 ... ";
    assert(sqrt(input) == output);
    std::cout << "Success!" << endl;

    input = 1238;
    output = std::sqrt(input);
    std::cout << "Begin test 7 ... ";
    assert(sqrt(input) == output);
    std::cout << "Success!" << endl;

    input = 12303;
    output = std::sqrt(input);
    std::cout << "Begin test 8 ... ";
    assert(sqrt(input) == output);
    std::cout << "Success!" << endl;

    return 0;
}