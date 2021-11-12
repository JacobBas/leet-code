#include <iostream>
#include <vector>
#include <unordered_map>
#include <assert.h>

int findShortestSubArray(std::vector<int> &nums)
{
    // initialize out hash map
    std::unordered_map<int, std::vector<int>> i_map;
    int degree = 0, length = 50001, n, i;

    // populating the hash map with the unique values and indecies
    for (i = 0; i < nums.size(); i++)
        i_map[nums[i]].push_back(i);

    // looping through the values in the hash map
    for (auto iter = i_map.begin(); iter != i_map.end(); iter++)
    {
        // length of the current sub array
        n = 1 + iter->second[iter->second.size() - 1] - iter->second[0];

        // if the degree is higher then we set the length
        if (iter->second.size() > degree)
            degree = iter->second.size(), length = n;

        // if the degree is equal then we check if shorter and set
        else if (iter->second.size() == degree)
            if (n < length)
                length = n;
    }

    // returning out the final length value
    return length;
}

int main()
{
    std::vector<int> input;
    int output;

    input = {1, 2, 2, 3, 1};
    output = 2;
    std::cout << "Begin test 1 ... ";
    assert(findShortestSubArray(input) == output);
    std::cout << "Success!" << std::endl;

    input = {1, 2, 2, 3, 1, 4, 2};
    output = 6;
    std::cout << "Begin test 2 ... ";
    assert(findShortestSubArray(input) == output);
    std::cout << "Success!" << std::endl;

    input = {1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2};
    output = 9;
    std::cout << "Begin test 3 ... ";
    assert(findShortestSubArray(input) == output);
    std::cout << "Success!" << std::endl;

    return 0;
}