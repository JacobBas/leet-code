#include <iostream>
#include <vector>
#include <assert.h>
using namespace std;

int diagonalSum(vector<vector<int>> &mat)
{
    int n = mat.size(), sum = 0;

    for (int i = 0; i < n; i++)
        sum += mat[i][i] + mat[i][n - 1 - i];

    if (n % 2 != 0)
        sum -= mat[n / 2][n / 2];

    return sum;
}

int main()
{
    vector<vector<int>> input;
    int output;

    input = {{1, 2, 3},
             {4, 5, 6},
             {7, 8, 9}};
    output = 25;
    std::cout << "Begin test 1 ... ";
    assert(diagonalSum(input) == output);
    std::cout << "Success!" << endl;

    input = {{1, 1, 1, 1},
             {1, 1, 1, 1},
             {1, 1, 1, 1},
             {1, 1, 1, 1}};
    output = 8;
    std::cout << "Begin test 2 ... ";
    assert(diagonalSum(input) == output);
    std::cout << "Success!" << endl;

    input = {{5}};
    output = 5;
    std::cout << "Begin test 3 ... ";
    assert(diagonalSum(input) == output);
    std::cout << "Success!" << endl;

    return 0;
}