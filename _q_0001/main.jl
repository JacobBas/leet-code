import Test

function twoSum(nums::Vector{Int}, target::Int)::Vector{Int}
    # initializing the nums dictionary
    numsDict = Dict()

    # looping through the values in nums for O(n) time
    for i = 1:length(nums)
        value = target - nums[i]
        check = get(numsDict, value, nothing)
        if check !== nothing
            return [numsDict[value], i]
        else
            numsDict[nums[i]] = i
        end
    end
end

# settin up our tests
# we need to add one to all indecies since julia
# indexes values starting at 1 instead of 0
Test.@test twoSum([2, 7, 11, 15], 9) == [1, 2]
Test.@test twoSum([3, 2, 4], 6) == [2, 3]
Test.@test twoSum([3, 3], 6) == [1, 2]