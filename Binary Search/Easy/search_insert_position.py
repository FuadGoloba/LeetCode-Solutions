"""
    35. Search Insert Position
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
    
    Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
    
    Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
    
    Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
"""

def searchInsert(nums: list[int], target: int) -> int:
    '''
        Return the index of the target if found in the sorted array, otherwise return the index where it would be if it were inserted in order.
        
        Intuition:
        We can use binary search to find the target in O(log n) time. If we find the target, we return its index. 
        If we don't find the target, we return the index where it would be inserted in order, which is the value of low at the end of the search.
        We return low because, even if target is not found,
            a. for target > nums[mid], we move low to mid + 1, which means low will be at the position where target would be inserted in order.
            b. for target < nums[mid], we move high to mid - 1, which means low will still be at the position where target would be inserted in order.       
        
        Steps:
        1. Initialize two pointers, low and high, to represent the current search range.
        2. While low is less than or equal to high:
            - Calculate the mid index.
            - If nums[mid] is equal to target, return mid.
            - If nums[mid] is less than target, move the low pointer to mid + 1.
            - If nums[mid] is greater than target, move the high pointer to mid - 1.
        3. If we exit the loop without finding the target, low will be at the position where the target would be inserted in order, so we return low
        
        Time Complexity: O(log n) due to binary search.
        Space Complexity: O(1) as we are using only a constant amount of space.    
    '''
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 5)) # 2
    print(searchInsert([1,3,5,6], 2)) # 1
    print(searchInsert([1,3,5,6], 7)) # 4
    print(searchInsert([1,3,5,6], 0)) # 0