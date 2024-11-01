""" Remove Duplicates from Sorted Array

    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    1. Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    2. Return k.

    Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
    
    Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
    
    
    SOLUTION:
    The intuition is to use two pointers, left and right. The right pointer is used to traverse the array while the left pointer keeps track of the current index where a unique element should be placed.
    The right pointer is initialised to be the 1; the index of second element in the array in order to compare with the previous element if they are equal or not. If not equal, then we have found a new unique elemnt and
    keep that elemnt in the position of the current unique index. If equal, then we know its a dupe and we continue traversing.
"""

def removeDuplicates(nums: list[int]) -> int:
    """Remove Duplicates from Sorted Array using while loop

    Args:
        nums (list[int]): integer array sorted in ascending order

    Returns:
        int: number of unique elements in nums
    """
    nums_length = len(nums)
    left_pointer, right_pointer = 1, 1 # Two pointers; left for tracking unique elements and right for traversing array

    # Traverse the array starting from the second element and compare with the previous element
    while right_pointer < nums_length:
        if nums[right_pointer] != nums[right_pointer - 1]: # New unique element found
            nums[left_pointer] = nums[right_pointer] # update the position of the new unique element by overwriting a dupe
            left_pointer += 1 
        right_pointer += 1
    return left_pointer

def removeDuplicates2(nums: list[int]) -> int:
    """Remove Duplicates from Sorted Array using for loop

    Args:
        nums (list[int]): integer array sorted in ascending order

    Returns:
        int: number of unique elements in nums
    """
    left_ptr = 1
    for right_ptr in range(1, len(nums)):
        if nums[right_ptr] != nums[right_ptr - 1]:
            nums[left_ptr] = nums[right_ptr]
            left_ptr += 1
    
    return left_ptr


if __name__ == "__main__":
    for nums in [ [1,1,2], [0,0,1,1,1,2,2,3,3,4], [1], [-3,-1,0,0,0,3,3] ]:
        print(removeDuplicates(nums), nums)