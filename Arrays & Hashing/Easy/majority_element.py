# Majority Element {EASY}
#   Given an array nums of size n, return the majority element.
#   The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majorityElement1(nums):
    '''
        Traversing the array 2xce in search for majority elements; Time = O(n2), Memory = O(1)
    '''
    for idx1 in range(len(nums)):
        counter = 1
        for idx2 in range(idx1 + 1, len(nums)):
            if nums[idx1] == nums[idx2]:
                counter += 1
        if counter > len(nums) // 2:
            return nums[idx1]
        
def majorityElement2(nums):
    '''
        Using a hasmap; Time = 0(n), Memory = O(n)
    '''
    # Create a dictionary to map each number to its frequency and return if its the majority element in the array
    counter_dict = {}
    for num in nums:
        counter_dict[num] = counter_dict.get(num, 0) + 1
        if counter_dict[num] > len(nums)//2:
            return num
        
def majorityElement2_1(nums):
    '''
        Using a hasmap; Time = 0(n), Memory = O(n)
    '''
    import collections
    counter = collections.Counter(nums)
    return max(counter.keys(), key=counter.get)

def majorityElement3(nums):
    '''
        Sorting the array and returning the element at index len(nums)//2 ; Time = O(nlogn), Memory = O(1)
    '''
    nums.sort()
    return nums[len(nums)//2]    

def majorityElement4(nums):
    '''
        Using Divide and Conquer Algorithm; Time = O(nlogn), Memory = O(logn)
    '''
    pass
        
    
if __name__ == '__main__':
    for arr in [[3,2,3],[2,2,1,1,1,2,2]]:
        print(majorityElement3(arr))