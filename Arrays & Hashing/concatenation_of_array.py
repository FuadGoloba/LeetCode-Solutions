# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]


def getConcatenation(nums):
    '''
        Time complexity - O(2n) = O(n)
    '''
    return 2 * nums

def getConcatenation2(nums):
    ans = []
    for idx in range(2):
        for num in nums:
            ans.append(num)
    return ans

if __name__ == '__main__':
    print(getConcatenation([1,3,2,1]))
    print(getConcatenation2([1,3,2,1]))