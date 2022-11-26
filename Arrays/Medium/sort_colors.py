# Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

def sortColors(nums):
    # Using Counting Sort Algorithm
    
    # Initialise an array, to keep track of each element's or color's count/freq
    freq = [0,0,0]

    # Get freq of each element in the nums array such that the index of freq array represents a distinct element in nums, and the value at that index represents the frequency
    # e.g freq = [2,1,2] means that nums array contains distinct elements 0, 1, 2 and 0 appears 2times, 1 appears 1 time and 2 appears 2times
    for ele in nums:
        freq[ele] += 1
        
    # Overwrite the nums array with the sorted elements
    idx = 0 # Initialise an idx to keep track of each index posn in nums array to overwrite 
    for ele in range(len(freq)): # Loop through the freq array as this represents the distinct elements of nums
        # For each distinct element, get it's freq and populate element, freq no of times into the nums array
        for j in range(freq[ele]): 
            nums[idx] = ele
            idx += 1 # move to the next index posn in the nums array to populate/overwrite
            
    return nums


if __name__ == '__main__':
    for nums in [[2,0,0,1,2], [2,2,1,0,1,1,0],]:
        print(sortColors(nums))
        
