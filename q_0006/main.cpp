#include <iostream>
using namespace std;

string convert(string s, int numRows)
{
    if (numRows == 1)
        return s;

    string rows[numRows];
    int i = 0, j = 0, dir = 1;
    while (i < s.size())
    {
        rows[j] += s[i];
        if (j == (numRows - 1))
            dir = -1;

        if (j == 0)
            dir = 1;

        j += dir;
        i++;
    }

    s = "";
    for (int i = 0; i < numRows; i++)
        s += rows[i];

    return s;
}

int main()
{
    cout << convert("PAYPALISHIRING", 4) << endl;
}