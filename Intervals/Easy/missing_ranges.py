"""
    Missing Ranges
    You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
    A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

    Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

    Example 1:
    Input: nums = [0,1,3,50,75], lower = 0, upper = 99
    Output: [[2,2],[4,49],[51,74],[76,99]]
    Explanation: The ranges are:
    [2,2]
    [4,49]
    [51,74]
    [76,99]

    Example 2:
    Input: nums = [-1], lower = -1, upper = -1
    Output: []
    Explanation: There are no missing ranges since there are no missing numbers.

    Constraints:
    -10^9 <= lower <= upper <= 10^9
    0 <= nums.length <= 100
    lower <= nums[i] <= upper
    All the values of nums are unique.
"""

def findMissingRanges(nums: list[int], lower: int, upper: int) -> list[list[int]]:
    """Return the shortest sorted list of ranges that exactly covers all the missing numbers using Two Pointers.
    
    Intuition:
    There are three places where gaps can occur: before the first element, between consecutive elements, and after the last element. By checking each of these locations, we can collect all missing ranges in a single pass.

    We can use two pointers to find the missing ranges between the numbers in the array. We can also add a dummy number at the beginning of the array to handle the case where the first number
    is greater than the lower bound. We can then iterate through the array and find the missing ranges between the numbers. Finally, we can check if there is a missing range between the last number in the array and the upper bound.
    
    Steps:
    1. Create a copy of the input array and insert a dummy number at the beginning, which is one less than the lower bound. This helps to handle the case where the first number is greater than the lower bound.
    2. Initialize two pointers, l and r, to the first and second elements of the modified array, respectively.
    3. While we traverse the modified array with the right pointer:
        a. If the difference between the current right pointer and the left pointer is greater than 1, it means there is a missing range between these two numbers. We can add this range to the result list.
        b. Move both pointers to the right to continue checking for missing ranges.
    4. After the loop, check if there is a missing range between the last number in the modified array and the upper bound. If there is, add this range to the result list.
    5. Return the result list containing all the missing ranges.    
    
    Time complexity: O(n) where n is the length of the input array, since we are traversing the array once.
    Space complexity: O(n) in the worst case, if all numbers in the range are missing, we will have n missing ranges. Otherwise, it is O(1) if there are no missing ranges or a constant number of missing ranges.
    
    """
    
    result = []
    l, r = 0, 1

    nums_copy = nums[:] # create a copy of the input array to avoid modifying the original array
    nums_copy.insert(0, lower - 1) # insert a dummy number at the beginning of the array to handle the case where the first number is greater than the lower bound

    while r < len(nums_copy):
        if nums_copy[r] - nums_copy[l] > 1:
            result.append([nums_copy[l] + 1, nums_copy[r] - 1])
        l += 1
        r += 1

    # After the loop, check if there is a missing range between the last number in the modified array and the upper bound. If there is, add this range to the result list.
    if upper - nums_copy[l] > 0:
        result.append([nums_copy[l] + 1, upper])

    return result

def findMissingRangesOptimal(nums: list[int], lower: int, upper: int) -> list[list[int]]:
    """Return the shortest sorted list of ranges that exactly covers all the missing numbers using Two Pointers and no extra copy.
    
    Intuition:
    There are three places where gaps can occur: before the first element, between consecutive elements, and after the last element. By checking each of these locations, we can collect all missing ranges in a single pass.

    Steps:
    1. If the array is empty, the entire range [lower, upper] is missing. Return it as a single range.
    2. Initialize two pointers, l and r, to the first and second elements of the array, respectively.
    2. Before first element: 
        Check if there is a gap between lower and nums[0]. If lower < nums[0], add [lower, nums[0] - 1] to the result.
    3. Between consecutive elements: 
        Iterate through consecutive pairs in the array. For each pair (nums[l], nums[r]):
            If the difference is greater than 1, there is a gap. Add [nums[l] + 1, nums[r] - 1] to the result.
    4. After last element:
        Check if there is a gap between last element nums[n - 1] (i.e nums[r - 1]) and upper. If upper > nums[n - 1], add [nums[n - 1] + 1, upper] to the result.
    5. Return the list of missing ranges.
    
    Time complexity: O(n) where n is the length of the input array, since we are traversing the array once.
    Space complexity: O(n) in the worst case, if all numbers in the range are missing, we will have n missing ranges. Otherwise, it is O(1) if there are no missing ranges or a constant number of missing ranges.
    """

    l, r, n = 0, 1, len(nums)
    result = []
    
    # If the array is empty, the entire range [lower, upper] is missing. Return it as a single range.
    if n == 0:
        return [[lower, upper]]

    # handling missing range before the first element (i.e between lower and nums[0])
    if nums[0] > lower:
        result.append([lower, nums[0] - 1])

    # handling missing ranges between consecutive elements (i.e between nums[l] and nums[r])
    while r < n:
        if nums[r] - nums[l] > 1:
            result.append([nums[l] + 1, nums[r] - 1])
        l += 1
        r += 1

    # handling missing range after last element (i.e between nums[n - 1] or nums[r - 1] and upper)
    if upper - nums[n - 1] > 0:
        result.append([nums[n - 1] + 1, upper])

    return result

def findMissingRangesOptimal2(nums: list[int], lower: int, upper: int) -> list[list[int]]:
    """Return the shortest sorted list of ranges that exactly covers all the missing numbers using for loop.

    Intuition:
    We can find missing ranges in the sorted array. We can check for missing ranges before the first element, between consecutive elements, and after the last element.

    Steps:
    1. Initialize an empty list to store the result.
    2. Check for missing range before the first element of the array. If there is a missing range, add it to the result list.
    3. Iterate through the array and check for missing ranges between consecutive elements. If there is a missing range, add it to the result list.
    4. Check for missing range after the last element of the array. If there is a missing range, add it to the result list.
    5. Return the result list containing all the missing ranges.

    Time complexity: O(n) where n is the length of the input array, since we are traversing the array once.
    Space complexity: O(n) in the worst case, if all numbers in the range are missing, we will have n missing ranges. Otherwise, it is O(1) if there are no missing ranges or a constant number of missing ranges.
    
    """
    
    result = []

    # Check for missing range before the first element of the array
    if nums and nums[0] > lower:
        result.append([lower, nums[0] - 1])

    # Check for missing ranges between consecutive elements
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            result.append([nums[i - 1] + 1, nums[i] - 1])

    # Check for missing range after the last element of the array
    if nums and nums[-1] < upper:
        result.append([nums[-1] + 1, upper])
    
    return result

if __name__ == "__main__":
    for func in [findMissingRanges, findMissingRangesOptimal, findMissingRangesOptimal2]:
        print(func([0,1,3,50,75], 0, 99)) # [[2,2],[4,49],[51,74],[76,99]]
        print(func([-1], -1, -1)) # []
        print(func(nums=[-1], lower=-2, upper=-1)) # [[-2, -2]]
        assert func([0,1,3,50,75], 0, 99) == [[2,2],[4,49],[51,74],[76,99]]
        assert func([-1], -1, -1) == []
        assert func(nums=[-1], lower=-2, upper=-1) == [[-2, -2]]
        
    