#include <iostream>
using namespace std;

int minSwaps(string s)
{
    bool check[s.size()];
    std::fill_n(check, s.size(), false);
    for (int i = 1; i < s.size() - 1; i++)
    {
        if (s[i] == s[i - 1] && (check[i - 1] == 0 || s[i] == s[i + 1]))
            check[i] = true;
    };

    int switches = 0;
    for (int i = 0; i < s.size(); i++)
        switches += check[i];

    if (switches % 2 == 0)
        switches /= 2;
    else
        switches = -1;

    return switches;
}

int main()
{
    cout << "===========================" << endl;
    cout << minSwaps("111000") << endl;
    cout << "===========================" << endl;
    cout << minSwaps("010") << endl;
    cout << "===========================" << endl;
    cout << minSwaps("1110") << endl;
    cout << "===========================" << endl;
    cout << minSwaps("1001") << endl;
    return 0;
}

// 11110000 01100101