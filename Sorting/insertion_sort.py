def insertion_sort(nums):
    """
        Idea:
        The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
        Time => Best case : O(n), Worst case : O(n2)
    """
    
    # Iterate through array fron the second index to the len(nums)
    for curr_idx in range(1, len(nums)):
        prev_idx = curr_idx - 1 # initialise a pointer to track the prev index
        
        # Swap prev element and curr element wherever curr elememnt is smaller than prev element until curr element is at it's rightful position
        while prev_idx >= 0 and nums[curr_idx] < nums[prev_idx]:
            nums[curr_idx], nums[prev_idx] = nums[prev_idx], nums[curr_idx] # swapping elements
            prev_idx -= 1
            curr_idx -= 1
    
    # return sorted array   
    return nums

if __name__ == '__main__':
    for nums in [[12, 11, 13, 5, 6], [1,2,4,3,1], [1,2,3], [1], [7,3,7]]:
        print(insertion_sort(nums))
            