# 3Sum Problem

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#   Notice that the solution set must not contain duplicate triplets.


# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2]. Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

def threeSum1(nums):
    '''
        Using the 2sum solution and an extra array ; Time = O(n2logn), Memory = O(n)
    '''
    result = [] # create a result list to store all triplets

    # Fix one of the numbers of the triplets and treat the rest of the solution as a Two-Sum (i.e Fix x and apply twosum on y and z)
    # Traverse the list, fixing each element
    for i in range(len(nums)): 
        target = 0 - nums[i] # Get the target for the TwoSm of y and Z (Since sum of triplets must give 0))
        hashset  = set() # Create a Hashset to track numbers traversed
        
        
        # Two Sum solution for y and z
        for j in range(i + 1, len(nums)):
            remainder = target - nums[j]
            if remainder in hashset:
                inner_list = [] # An inner list to store individual triplet
                inner_list.extend(sorted([nums[i], nums[j], remainder]))
                # Check that inner list only contains three sum and the result list contains no duplicates
                if inner_list not in result:
                    result.append(inner_list)
                # OR 
                # result.append(sorted([nums[i], nums[j], remainder])) if sorted([nums[i], nums[j], remainder]) not in result else None
            else:
                hashset.add(nums[j])
    return result


def threeSum2(nums):
    '''
        Using Two Pointer solution and TwoSum II solution; Time = O(n2), memory = O(n)
    '''

    result = [] # Result list to store 3sum
    nums.sort() # Sort list in ascending order to keep duplicates adjacent to one another
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]: # Check that we don't fix an element that has been fixed previously (Skip duplicate element)
            continue
        
        #### Now we have a Two Sum solution
        # Initialise left and right pointers
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        
        # Run a loop until left pointer is less than right if the sum of triplets equal 0 and append to the result
        while left < right:
            if nums[left] + nums[right] < target: # If the sum is less then the target, then we move the left pointer to the next element; thus increasing the sum since the array is sorted
                left += 1
            elif nums[left] + nums[right] > target: # If the sum is greater then the target, then we move the right pointer to the lement before; thus reducing the sum 
                right -= 1
            
            # Here we get the three sum and we append the elements into the result and shift the left pointer to the next adjacent element   
            else:
                result.append([nums[i], nums[left], nums[right]])   
                left += 1
                
                # We have to check that the element of the next left pointer is not same as the previous one (not duplicate)
                while nums[left] == nums[left - 1] and left < right: # if duplcate value of left pointer, we skip and shift the left pointer forward
                    left += 1     
    return result

if __name__ == '__main__':
    for nums in [[-1,0,1,2,-1,-4], [0,1,1],[0,0,0]]:
        print(threeSum2(nums))
    
        