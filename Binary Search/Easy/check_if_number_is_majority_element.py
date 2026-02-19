"""
    Check If a Number Is Majority Element in a Sorted Array
    Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.
    A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

    Example 1:
    Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
    Output: true
    Explanation: The value 5 appears 5 times and the length of the array is 9. 
    Thus, 5 is a majority element because 5 > 9/2 is true.

    Example 2:
    Input: nums = [10,100,101,101], target = 101
    Output: false
    Explanation: The value 101 appears 2 times and the length of the array is 4. 
    Thus, 101 is not a majority element because 2 > 4/2 is false.

    Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i], target <= 10⁹
    nums is sorted in non-decreasing order.

"""

def isMajorityElement(nums: list[int], target: int) -> bool:
    """Return true if target is a majority element in the sorted array, or false otherwise.

    Intuition:
    We can iterate through the array and count the occurrences of the target. If the count is greater than half of the length of the array, then it is a majority element.

    Steps:
    1. Initialize a count variable to 0.
    2. Iterate through the array and increment the count variable each time we encounter the target.
    3. After the loop, check if the count is greater than half of the length of the array. If it is, return true, otherwise return false.

    Time Complexity: O(n) as we need to iterate through the array once.
    Space Complexity: O(1) as we are using only a constant amount of space.
    """
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count > len(nums) / 2


def isMajorityElementOptimized(nums: list[int], target: int) -> bool:
    """Return true if target is a majority element in the sorted array, or false otherwise.

    Intuition:
    We can use binary search to find the first occurrence of the target in the sorted array. If the target is a majority element, it must appear at index first + n // 2, because if it appears more than n // 2 times, it must span across the middle of the array. For example, if n = 9 and target appears 5 times, it must appear at index first + 4, which is the middle of the array. If n = 10 and target appears 6 times, it must appear at index first + 5, which is also the middle of the array. Therefore, we can check if target is a majority element by checking if it appears at index first + n // 2.

    Steps:
    1. Use binary search to find the first occurrence of the target in the array.
    2. If the target is not found, return false.
    3. If the target is found, check if it appears at index first + n // 2. If it does, return true, otherwise return false.
    4. We need to check if first + n // 2 is within the bounds of the array before checking if it is equal to target, otherwise we might get an index out of bounds error.
    5. Return false if first + n // 2 is out of bounds or if nums[first + n // 2] is not equal to target.
    6. Return true if nums[first + n // 2] is equal to target.

    Time Complexity: O(log n) due to binary search.
    Space Complexity: O(1) as we are using only a constant amount of space.
    """

    def firstOccurrence(nums, target):
        """Returns the index of the first occurrence of target"""
        l, r = 0, len(nums) - 1
        index = -1  # we don't find the target, return -1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                index = mid  # we want to find the first occurrence, so we continue searching in the left half and update the index
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return index

    n = len(nums)
    first = firstOccurrence(nums, target)
    # If target is a majority element, it must appear at index first + n // 2, because if it appears more than n // 2 times, it must span across the middle of the array.
    ## If target exists, check if it still exists half-a-length away
    if first != -1 and first + (n // 2) < n:
        return nums[first + (n // 2)] == target
    return False


def isMajorityElement_simple(nums: list[int], target: int) -> bool:
    """Return true if target is a majority element in the sorted array, or false otherwise.

    Intuition:
    We can use binary search to find the first and last occurrence of the target in the sorted array.
    If the count of the target (last occurrence index - first occurrence index + 1) is greater than half of the length of the array, then it is a majority element.

    Steps:
    1. Check the middle element of the array. If it is not equal to the target, then the target cannot be a majority element, because if it were a majority element, it would have to be at the middle index.
    2. Use binary search to find the first occurrence of the target in the array.
    3. Use binary search to find the last occurrence of the target in the array.
    4. Calculate the count of the target as (last occurrence index - first occurrence index + 1).
    5. Return true if count > len(nums) / 2, otherwise return false.

    Time Complexity: O(log n) due to binary search.
    Space Complexity: O(1) as we are using only a constant amount of space.
    """

    def lastOccurrence(nums, target):
        """Returns the index of the last occurrence of target"""
        l, r = 0, len(nums) - 1
        index = -1  # we don't find the target, return -1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                index = mid  # we want to find the last occurrence, so we continue searching in the right half and update the index
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return index

    def firstOccurrence(nums, target):
        """Returns the index of the first occurrence of target"""
        l, r = 0, len(nums) - 1
        index = -1  # we don't find the target, return -1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                index = mid  # we want to find the first occurrence, so we continue searching in the left half and update the index
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return index

    # It's intuitive that for a sorted array, if target is a majority element, it must exist at mid_index, otherwise it cannot be a majority element.
    mid_idx = len(nums) // 2
    if nums[mid_idx] != target:
        return False

    first, last = firstOccurrence(nums, target), lastOccurrence(nums, target)
    return ((last - first) + 1) > len(nums) / 2


# first_idx = lower_bound(nums, target)
# if first_idx == -1:
#     return False

# # If it is majority, it MUST span at least this far
# check_idx = first_idx + (len(nums) // 2)
# return check_idx < len(nums) and nums[check_idx] == target


def isMajorityElement2(nums: list[int], target: int) -> bool:
    """
    Return true if target is a majority element in the sorted array, or false otherwise.

    Intuition:
    We can use binary search to find the first and last occurrence of the target in the sorted array.
    If the count of the target (last occurrence index - first occurrence index + 1) is greater than half of the length of the array, then it is a majority element.

    Steps:
    1. Use binary search to find the first occurrence of the target in the array.
    2. Use binary search to find the last occurrence of the target in the array.
    3. Calculate the count of the target as (last occurrence index - first occurrence index + 1).
    4. Return true if count > len(nums) / 2, otherwise return false.

    Time Complexity: O(log n) due to binary search.
    Space Complexity: O(1) as we are using only a constant amount of space.
    """

    def findFirstOccurrence(nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low  # low will be at the position of the first occurrence of target if it exists, otherwise it will be at the position where target would be inserted in order.

    def findLastOccurrence(nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return high  # high will be at the position of the last occurrence of target if it exists, otherwise it will be at the position where target would be inserted in order minus one.
    
    mid_idx = len(nums) // 2
    if nums[mid_idx] != target:
        return False

    first_occurrence = findFirstOccurrence(nums, target)
    last_occurrence = findLastOccurrence(nums, target)
    count = last_occurrence - first_occurrence + 1
    return count > len(nums) / 2

if __name__ == "__main__":
    nums = [2, 4, 5, 5, 5, 5, 5, 6, 6]
    target = 5
    print(isMajorityElement(nums, target))  # True
    print(isMajorityElementOptimized(nums, target))  # True
    print(isMajorityElement_simple(nums, target))  # True
    print(isMajorityElement2(nums, target))  # True

    nums = [10,100,101,101]
    target = 101
    print(isMajorityElement(nums, target))  # False
    print(isMajorityElementOptimized(nums, target))  # False
    print(isMajorityElement_simple(nums, target))  # False
    print(isMajorityElement2(nums, target))  # False
    
    assert isMajorityElement(nums, target) == False
    assert isMajorityElementOptimized(nums, target) == False
    assert isMajorityElement_simple(nums, target) == False
    assert isMajorityElement2(nums, target) == False
