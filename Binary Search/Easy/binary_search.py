# BINARY SEARCH {EASY} 
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1



def search(nums, target):
    # Using Recursion    
    def binarySearch_recursion(key, array, left_index, right_index):    
        # Base case
        if right_index >= left_index: 
            
            # Get the middle index
            mid_index = (left_index + right_index) // 2
            
            if key == array[mid_index]: # Check that the value at the mid index is the key and return it's index
                return mid_index
            
            if key < array[mid_index]: # Check that the key is in the lower limit of the array, lower than the middle number and reduce the search to only the left side
                right_index = mid_index - 1
            
            elif key > array[mid_index]: # Check that the key is in the upper limit of the array higher than the middle number and reduce the search to the upper limit
                left_index = mid_index + 1
            # recursively search for the key in the upper or lower limit 
            return binarySearch_recursion(key, array, left_index, right_index)
        else:
            return -1
    
    # run binarysearch recursively on the array
    return binarySearch_recursion(target, nums, 0, len(nums))
    

def binarySearch_iterative(array, key):
    
    left_index = 0 # Initialise a pointer to track the left most side of the array
    right_index = len(array) - 1 # initialise a pointer to track the right most side of the array
    
    # Iterate until we've shrunk the search space
    while left_index <= right_index:
        # Get the middle of the array to serve as a mid point for comparison and reducing the search space
        mid_index = (left_index + right_index) // 2
        
        # If the target is same as the element at the middle index, then we have found our target
        if key == array[mid_index]:
            return mid_index
        
        # If the target is less than the element at the midpoint, then we only search the left side (which is the lower side of the array)
        if key < array[mid_index]:
            right_index = mid_index - 1
        # if the target is greater than the element at the midpoint, then we only search the right side 
        else:
            left_index = mid_index + 1
            
    return -1

if __name__ == '__main__':
    
    for (nums, target) in [([1,2,5,7,8,24,45,56], 5), ([2,3,5,7,9,34], 0),]:
        print(binarySearch_iterative(nums, target))