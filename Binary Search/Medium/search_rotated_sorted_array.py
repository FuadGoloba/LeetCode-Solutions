# Search in Rotated Sorted Array {MEDIUM}

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1



def searchRotatedSortedArray(nums, target):
    
    '''
        Using Binary Search iterative method - Time = O(logn), Memory = O(1)
    '''
    
    left_index = 0
    right_index = len(nums) - 1
    
    # Run loop until shifting left index meets right index
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2 # Get the middle index
        
        # Check if the value at the middle index is the value we're searching
        if target == nums[mid_index]:
            return mid_index
        
        # Check if the left portion of the array is sorted (If the value at left is less than the value at the mid; then the array from left to mid is sorted )
        if nums[mid_index] >= nums[left_index]: 
            # if the target doesn't lie in the range from nums[left] to nums[mid] (left sorted portion), then we move our search space to the right area
            if  target < nums[left_index] or target > nums[mid_index]: 
                left_index = mid_index + 1 # we shift our starting index to the right side and search 
            # else if the target does lie in the left portion, then we continue our search in the left area
            else:
                right_index = mid_index - 1 # We shift our 
        
        # Check the right sorted portion of the array (If the value at the right is greater than the value at the middle, then the array from mid+1 to right is sorted)
        else: 
            # if the target doesn't lie in the right sorted portion, we move our search in the left area
            if target > nums[right_index] or target < nums[mid_index]:
                right_index = mid_index - 1
            # if the target does lie in the right portion, we continue our search in the right area
            else:
                left_index = mid_index + 1
            
    return -1


if __name__ == '__main__':
    for nums, target in [([4,5,6,7,0,1,2], 0), ([4,5,6,7,0,1,2], 3), ([1], 0)]:
        print(searchRotatedSortedArray(nums, target))