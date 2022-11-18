# Contains Duplicate - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. {EASY}

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def containsDuplicate1(nums):
    '''
        Naive Solution = Time - O(n2), Memory - O(1)
    '''
    for idx1 in range(len(nums)):
        for idx2 in range(idx1 + 1, len(nums)):
            if nums[idx1] == nums[idx2]:
                return True   
    return False

def containsDuplicate2(nums):
    '''
        Sliding Window Method; Time - O(nlogn), Memory - O(1)
    '''
    nums.sort()  # Sort the list so duplicates will stay adjacent to one another if there axists any
    left_ptr = 0 # Initialise a left pointer
    right_ptr = 1 # Initialise a right pointer
    
    # Loop until the end of the array/list
    while right_ptr < len(nums):
        # check that the adjacent neighbours are duplicates else slide or shift to the next pointer
        if nums[left_ptr] == nums[right_ptr]:
            return True
        # slide the lelft pointer to the right
        left_ptr = right_ptr
        # move the right pointer to the right
        right_ptr += 1
    return False
    

def containsDuplicate3(nums):
    '''
        Using a hashset; Time - O(n), Memory - O(n)
    '''
    
    return len(set(nums)) != len(nums)

def containsDuplicate4(nums):
    '''
        Using a hashset; Time - O(n), Memory - O(n)
    '''
    hashset = set()
    # Loop through items in the array/list
    for item in nums:
        # Cjeck that the item already exists in the hashset which means there's a duplicate
        if item in hashset:
            return True
        # else add the item to the hashset
        hashset.add(item)
    return False
            

if __name__ == '__main__':
    for input_n in [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]:
        print(containsDuplicate4(input_n))                             