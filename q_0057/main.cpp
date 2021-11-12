#include <iostream>
#include <vector>
#include <algorithm>
#include <assert.h>
using namespace std;

// worst case scenario is when we have to insert a value in at index 1 since
// we then check every value and then also have to shift all values of the
// vector for the new index
vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
{
    if (intervals.size() == 0)
        intervals.push_back(newInterval);

    else if (newInterval[1] < intervals[0][0])
        intervals.insert(intervals.begin(), newInterval);

    else
    {
        int lower_i = intervals.size(); // index that fits lower
        int upper_i = 0;                // index that fits upper

        // assigning the lower_i and upper_i
        for (int i = 0; i < intervals.size(); i++)
        {
            if (newInterval[0] <= intervals[i][1])
                lower_i = std::min(i, lower_i);
            if (newInterval[1] >= intervals[i][0])
                upper_i = i;
        }

        // appending newInterval to the end
        if (lower_i == intervals.size())
            intervals.push_back(newInterval);

        else
        {
            // assigning values to newInterval
            newInterval[0] = std::min(intervals[lower_i][0], newInterval[0]);
            newInterval[1] = std::max(intervals[upper_i][1], newInterval[1]);

            if (lower_i > upper_i)
                intervals.insert(intervals.begin() + lower_i, newInterval);

            else
            {
                // removing the old indecies while keeping one to use as
                // a replacement from the new interval
                intervals.erase(intervals.begin() + lower_i + 1, intervals.begin() + upper_i + 1);

                // inserting the new index
                intervals[lower_i][0] = newInterval[0];
                intervals[lower_i][1] = newInterval[1];
            }
        }
    }

    return intervals;
}

int main()
{
    vector<vector<int>> intervals, output;
    vector<int> newInterval;

    intervals = {{1, 3}, {6, 9}};
    newInterval = {2, 5};
    output = {{1, 5}, {6, 9}};
    std::cout << "Begin test 1" << endl;
    assert(insert(intervals, newInterval) == output);

    intervals = {{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}};
    newInterval = {4, 8};
    output = {{1, 2}, {3, 10}, {12, 16}};
    std::cout << "Begin test 2" << endl;
    assert(insert(intervals, newInterval) == output);

    intervals = {};
    newInterval = {5, 7};
    output = {{5, 7}};
    std::cout << "Begin test 3" << endl;
    assert(insert(intervals, newInterval) == output);

    intervals = {{1, 5}};
    newInterval = {2, 3};
    output = {{1, 5}};
    std::cout << "Begin test 4" << endl;
    assert(insert(intervals, newInterval) == output);

    intervals = {{1, 5}};
    newInterval = {2, 7};
    output = {{1, 7}};
    std::cout << "Begin test 5" << endl;
    assert(insert(intervals, newInterval) == output);

    intervals = {{1, 5}};
    newInterval = {6, 8};
    output = {{1, 5}, {6, 8}};
    std::cout << "Begin test 6" << endl;
    assert(insert(intervals, newInterval) == output);

    intervals = {{6, 8}};
    newInterval = {1, 5};
    output = {{1, 5}, {6, 8}};
    std::cout << "Begin test 7" << endl;
    assert(insert(intervals, newInterval) == output);

    intervals = {{3, 5}, {12, 15}};
    newInterval = {6, 6};
    output = {{3, 5}, {6, 6}, {12, 15}};
    std::cout << "Begin test 8" << endl;
    assert(insert(intervals, newInterval) == output);

    return 0;
}