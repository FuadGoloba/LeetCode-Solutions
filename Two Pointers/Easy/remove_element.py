""" Remove Element from Array

    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
    The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    1. Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    2. Return k.
    
    Example 1:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    
    Example 2:
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    
    SOLUTION:
    The intuition is to use to two pointers; left and right. The right pointer is used to traverse the array while the left pointer keeps track of the the position where the next non-target element should be placed (is also k)
    Both pointers are initialised to 0. During traversal by the right pointer, we overwrite the target elements with non-target elements at the position of the left pointer if not an occurrence of the target val, which then
    effectively removes all occurrences of the target value from the array.
"""

def removeElement(nums: list[int], val: int) -> int:
    """Remove elements from Array using while loop
    
    Time Complexity - O(n)

    Args:
        nums (list[int]): integer array
        val (int): target integer value

    Returns:
        int: number of non-target values in nums
    """
    left_ptr, right_ptr = 0, 0 # left tracks position where the next non-target element should be placed and right traverses the array
    nums_length = len(nums)
    
    # Traverse the array and overwrite target elements with nonj-target elements
    while right_ptr < nums_length:
        if nums[right_ptr] != val:
            nums[left_ptr] = nums[right_ptr]
            left_ptr += 1
        right_ptr += 1
    return left_ptr


def removeElement2(nums: list[int], val: int) -> int:
    """Remove elements from Array using for loop
    
    Time Complexity - O(n)

    Args:
        nums (list[int]): integer array
        val (int): target integer value

    Returns:
        int: number of non-target values in nums
    """
    left_ptr = 0
    nums_length = len(nums)
    
    # Traverse the array and overwrite target elements with nonj-target elements
    for right_ptr in range(nums_length):
        if nums[right_ptr] != val:
            nums[left_ptr] = nums[right_ptr]
            left_ptr += 1
    return left_ptr

if __name__ == '__main__':
    for nums, val in [ ([3,2,2,3], 3), ([0,1,2,2,3,0,4,2], 2) ]:
        print(removeElement(nums, val))