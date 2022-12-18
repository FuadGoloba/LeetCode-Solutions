# Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

def findKthLargest1(nums, k):
    '''
        Using a sorting technique
        Time:  Best Case: O(n)
               Average Case: O(n*log(n))
               Worst Case:O(n*log(n))
        Extra Space Complexity: O(n)
    '''
    nums.sort() # Sort the array 
    return nums[len(nums) - k] 

def findKthLargest2(nums, k):
    '''
        Using a Heap Data structure
        Time = O(n)
        Memory = O(n)
    '''
    import heapq
    
    # Creating a minHeap of size K elements and popping from the heap till its of size k elements as the smallest element in the minHeap of size K is the Kth Largest element
    heapq.heapify(nums) # Heapify the array
    
    while len(nums) > k:
        heapq.heappop(nums)
        
    # Return the minimum element of the minHeap which is also the Kth largest element in the array
    return nums[0]


if __name__ == '__main__':
    for nums, k in [([3,2,1,5,6,4], 2), ([3,2,3,1,2,4,5,5,6], 4)]:
        print(findKthLargest2(nums, k))
    