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
"""

def removeDuplicates(nums: list[int]) -> int:
    """Remove Duplicates from Sorted Array using while loop with Two Pointers
    
        Intuition: 
            - Use two pointers to traverse the array. The right pointer iterates through the array, while the left pointer tracks the position where the next unique element should be placed.
            - When the right pointer encounters a new unique element (i.e., an element that is different from the previous one), it is copied to the position indicated by the left pointer, and the left pointer is incremented. This effectively overwrites duplicate elements with unique elements as the right pointer traverses the array.
            - After the right pointer has traversed the entire array, the left pointer will indicate the number of unique elements in the array, which is returned as the final result. 
            
        Steps:
            1. Initialize two pointers, left_pointer and right_pointer, to the start of the array (left_pointer starts at index 1 since the first element is always unique).
            2. While the right pointer is within the bounds of the array:
                - If the element at the right pointer is different from the element at the previous index (right_pointer - 1):
                    - Copy the element at the right pointer to the position indicated by the left pointer.
                    - Increment the left pointer to move to the next position for potential unique elements.
                - Increment the right pointer to continue traversing the array.
            3. Return the value of the left pointer, which represents the count of unique elements in the array.       
            
    Time Complexity - O(n) : We traverse the array once with the right pointer, resulting in O(n) time complexity, where n is the length of the input array nums.
    Space Complexity - O(1) : We use a constant amount of extra space for the two pointers.
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
    """Remove Duplicates from Sorted Array using for loop with Two Pointers

        Intuition:
            - Use two pointers to traverse the array. The right pointer iterates through the array, while the left pointer tracks the position where the next unique element should be placed.
            - When the right pointer encounters a new unique element (i.e., an element that is different from the previous one), it is copied to the position indicated by the left pointer, and the left pointer is incremented. This effectively overwrites duplicate elements with unique elements as the right pointer traverses the array.
            - After the right pointer has traversed the entire array, the left pointer will indicate the number of unique elements in the array, which is returned as the final result.
            
        Steps:
            1. Initialize a pointer, left_ptr, to the start of the array (left_ptr starts at index 1 since the first element is always unique).
            2. Use a for loop to iterate through the array starting from the second element (index 1):
                - If the current element (nums[right_ptr]) is different from the previous element (nums[right_ptr - 1]):
                    - Copy the current element to the position indicated by left_ptr.
                    - Increment left_ptr to move to the next position for potential unique elements.
            3. Return the value of left_ptr, which represents the count of unique elements in the array.        
            
    Time Complexity - O(n) : We traverse the array once with the right pointer, resulting in O(n) time complexity, where n is the length of the input array nums.
    Space Complexity - O(1) : We use a constant amount of extra space for the left pointer.
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