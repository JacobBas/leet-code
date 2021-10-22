#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> merge(vector<vector<int>> &intervals)
{
    // sorting the initial intervals
    std::sort(intervals.begin(), intervals.end());

    // initializing our response vector
    vector<vector<int>> resp;
    resp.push_back(intervals[0]);

    // merging the vectors where applicable
    for (int i = 1; i < intervals.size(); i++)
        if (resp[resp.size() - 1][1] >= intervals[i][0])
            resp[resp.size() - 1][1] = std::max(resp[resp.size() - 1][1], intervals[i][1]);
        else
            resp.push_back(intervals[i]);

    return resp;
}

int main()
{
    vector<vector<int>> vec1 = {{1, 3}, {2, 6}, {8, 10}};
    vector<vector<int>> resp1;
    resp1 = merge(vec1);
    for (int i = 0; i < resp1.size(); i++)
    {
        cout << resp1[i][0] << " - " << resp1[i][1] << ", ";
    }
    cout << endl;

    vector<vector<int>> vec2 = {{1, 4}, {4, 5}};
    vector<vector<int>> resp2;
    resp2 = merge(vec2);
    for (int i = 0; i < resp2.size(); i++)
    {
        cout << resp2[i][0] << " - " << resp2[i][1] << ", ";
    }
    cout << endl;

    vector<vector<int>> vec3 = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    vector<vector<int>> resp3;
    resp3 = merge(vec3);
    for (int i = 0; i < resp3.size(); i++)
    {
        cout << resp3[i][0] << " - " << resp3[i][1] << ", ";
    }
    cout << endl;

    vector<vector<int>> vec4 = {{1, 4}, {0, 5}};
    vector<vector<int>> resp4;
    resp4 = merge(vec4);
    for (int i = 0; i < resp4.size(); i++)
    {
        cout << resp4[i][0] << " - " << resp4[i][1] << ", ";
    }
    cout << endl;

    vector<vector<int>> vec5 = {{2, 3}, {4, 5}, {6, 7}, {8, 9}, {1, 10}};
    vector<vector<int>> resp5;
    resp5 = merge(vec5);
    for (int i = 0; i < resp5.size(); i++)
    {
        cout << resp5[i][0] << " - " << resp5[i][1] << ", ";
    }
    cout << endl;

    return 0;
}