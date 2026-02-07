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
"""

def removeElement(nums: list[int], val: int) -> int:
    """Remove elements from Array using Two Pointers
    
    Intuition:
        - Use two pointers to traverse the array. The right pointer iterates through the array, while the left pointer tracks the position where the next non-target element should be placed.
        - When the right pointer encounters a non-target element, it is copied to the position indicated by the left pointer, and the left pointer is incremented. This effectively overwrites target elements with non-target elements as the right pointer traverses the array.
        - After the right pointer has traversed the entire array, the left pointer will indicate the number of non-target elements in the array, which is returned as the final result. 
    
    Steps:
        1. Initialize two pointers, left_ptr and right_ptr, to the start of the array.
        2. While the right pointer is within the bounds of the array:
            - If the element at the right pointer is not equal to the target value:
                - Copy the element at the right pointer to the position indicated by the left pointer.
                - Increment the left pointer to move to the next position for potential non-target elements.
            - Increment the right pointer to continue traversing the array.
        3. Return the value of the left pointer, which represents the count of non-target elements in the array.
    
    Time Complexity - O(n)
    Space Complexity - O(1)
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
    """Remove elements from Array using Two Pointers (For Loop)
    
    Intuition:
        - Use two pointers to traverse the array. The right pointer iterates through the array, while the left pointer tracks the position where the next non-target element should be placed.
        - When the right pointer encounters a non-target element, it is copied to the position indicated by the left pointer, and the left pointer is incremented. This effectively overwrites target elements with non-target elements as the right pointer traverses the array.
        - After the right pointer has traversed the entire array, the left pointer will indicate the number of non-target elements in the array, which is returned as the final result.
        
    Steps:
        1. Initialize a pointer, left_ptr, to the start of the array to track the position where the next non-target element should be placed.
        2. Use a for loop to iterate through the array with a right pointer:
            - If the element at the right pointer is not equal to the target value:
                - Copy the element at the right pointer to the position indicated by the left pointer.
                - Increment the left pointer to move to the next position for potential non-target elements.
        3. Return the value of the left pointer, which represents the count of non-target elements in the array.
    
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    left_ptr = 0
    nums_length = len(nums)

    # Traverse the array and overwrite target elements with non-target elements
    for right_ptr in range(nums_length):
        if nums[right_ptr] != val:
            nums[left_ptr] = nums[right_ptr]
            left_ptr += 1
    return left_ptr

if __name__ == '__main__':
    for nums, val in [ ([3,2,2,3], 3), ([0,1,2,2,3,0,4,2], 2) ]:
        print(removeElement(nums, val))