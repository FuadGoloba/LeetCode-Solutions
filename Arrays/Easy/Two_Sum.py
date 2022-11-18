#Two Sum -  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. {EASY}
#           You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

def twoSum1(nums, target):
    '''
        Naive Solution = Time - O(n2), Memory - O(1)
    '''
    
    for idx1 in range(len(nums)):
        for idx2 in range(idx1 +1, len(nums)):
            if nums[idx1] + nums[idx2] == target:
                return [idx1, idx2]
            
        
def twoSum2(nums, target):
    '''
    Using a hashset; Time = O(n), memory - O(1)
    '''
    
    seen = {} #Hashmap to map each value to its index
    for index, value in enumerate(nums): # Loop through the array taking the value and its index
        remainder = target - value # get the difference between the target and the value
        if remainder in seen: # Check that the remainder already exists as a key in our hashmap (i.e check that the difference is a key that has been stored in the hashmap previosuly)
            return [index, seen[remainder]] # return the index of the remainder and the index of the current value in the list 
        seen[value] = index # # if it's not in the dictionary, store it in the dictionary
            
            
if __name__ == '__main__':
    for nums, target in [
        ([2,7,11,15], 9), ([3,2,4], 6), ([3,3], 6)
    ]:
        print(twoSum2(nums, target))