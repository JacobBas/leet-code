import Test

function reverseString(s::Vector{String})
    n = length(s)
    for i = 1:(floor(Int, n / 2))
        temp = s[i]
        s[i] = s[n+1-i]
        s[n+1-i] = temp
    end
end

println("Test 1:")
input = ["h", "e", "l", "l", "o"]
output = ["o", "l", "l", "e", "h"]
Test.@time reverseString(input)
Test.@test input == output

println("Test 2:")
input = ["H", "a", "n", "n", "a", "h"]
output = ["h", "a", "n", "n", "a", "H"]
Test.@time reverseString(input)
Test.@test input == output