# Counting Sort

# Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (a kind of hashing). 
# Then do some arithmetic operations to calculate the position of each object in the output sequence.

# Counting Sort, although faster than merge, insertion, quick, etc is mainly useful when input is distributed over a range e.g [2,0,0,1,2]. For example, consider the following problem. 
# Sort a large set of numbers which are in range from 0 to 5 and have repeated values across the range. [2,5,1,0,1,1,0]


def counting_sort(nums):
    '''
        Time = O(n) (Best and Worst); Memory = O(n)
    '''
    
    # Get the maximum element in nums
    max_ele = max(nums)
    
    # Initialise an array, the length of the maximum element to keep track of each element's count/freq
    freq = [0 for i in range(max_ele + 1)]
    
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
    for nums in [[2,0,0,1,2], [2,5,1,0,1,1,0],]:
        print(counting_sort(nums))
        