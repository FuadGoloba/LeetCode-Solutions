# QuickSort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. 
# There are many different versions of quickSort that pick pivot in different ways. 
        # Always pick the first element as a pivot
        # Always pick the last element as a pivot
        # Pick a random element as a pivot
        # Pick median as a pivot

# Here we will be picking the last element as a pivot. The key process in quickSort is partition(). 
# Target of partitions is, given an array we pick an element ‘x’ of array as a pivot, put x at its correct position in a sorted array
# and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time. 

# Running Time = O(nlogn) on average and at best, O(n2) at worst

def quick_sort(nums):
    
    # create a helper function - sortArray to recursively sort array using partition method
    #   start : index of first element
    #   end : index of last element
    
    def SortArray(nums, start, end):
        # recurse until there's just one element in the array
        if start < end:
            
            # Partition array by Finding pivot element such that element smaller than pivot are on the left, element greater than pivot are on the right
            # returns the index where partition is done
            partitioned_ptr = partition(nums, start, end)
            
            # Recursive call on the left of pivot
            SortArray(nums, start, partitioned_ptr - 1)
            
            # Recursive call on the right of pivot
            SortArray(nums, partitioned_ptr + 1, end)
    
    def partition(nums, start, end):
        # This implementation utilizes pivot as the last element in the nums list
        # It has a pointer to keep track of the elements smaller than the pivot
        # At the very end of partition() function, the pointer is swapped with the pivot to come up with a "sorted" nums relative to the pivot
        
        # Choose the last element as pivot to partition array
        pivot = nums[end]
        
        # Pointer to track elements larger than pointer in order to swap
        i = start - 1
        
        # Traverse through all elements except pivot, comparing each element with pivot
        for j in range(start, end):
            if nums[j] <= pivot:
                # If element smaller than pivot is found, swap it with the greater element pointed by i
                i += 1
                
                # Swapping element at i with element at j
                nums[i], nums[j] = nums[j], nums[i]
              
        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        
        # Return the position from where partition is done
        return i + 1
    
    # Execute helper function to sort array using partition
    SortArray(nums, 0, len(nums) - 1)   
    return nums # Return sorted array



# ---------------------------------- OR ------------------------------------------------------#
# def sortArray(nums):
#     if len(nums) < 1:
#         return nums

#     # Partition array by Finding pivot element such that element smaller than pivot are on the left element greater than pivot are on the right
#     # returns the partitioned array and index of partitioned element
#     partitioned_array, sorted_pivot = partition(nums)[0], partition(nums)[1]
    
#     # Recursive call on the left of pivot
#     sortArray(partitioned_array[:sorted_pivot])
#     # Recursive call on the right of pivot
#     sortArray(partitioned_array[sorted_pivot + 1:])
    
#     # return sorted array
#     return nums

# def partition(nums):
    
#     # This implementation utilizes pivot as the last element in the nums list
#     # It has a pointer to keep track of the elements smaller than the pivot
#     # At the very end of partition() function, the pointer is swapped with the pivot to come up with a "sorted" nums relative to the pivot
    
#     # Choose the last element as pivot to partition array
#     pivot_idx = -1
#     pivot = nums[pivot_idx]
    
#     # Initialise two pointers; left to track index of elements smaller than the pivot, and right to traverse the entire array
#     left = -1
#     right = 0
    
#     # Traverse through all elements bar pivot, comparing each element with pivot
#     while right < len(nums) - 1:
#         # Check that the curr element is smaller than the pivot and swap curr element with element in the left position, update left position to go to nect index
#         if nums[right] < pivot: 
#             left += 1 
#             nums[left], nums[right] = nums[right], nums[left]
        
#         right += 1
        
#     # At the end of the traversal, we put the pivot element at it's rightful position ; which is at the index pointer of the last partition element  
#     nums[left + 1], nums[pivot_idx] = nums[pivot_idx], nums[left + 1]
    
#     # Return the partitioned array and the position where partition was done
#     return nums, left + 1


if __name__ == '__main__':
    for nums in [[12, 11, 13, 5, 6], [1,2,4,1], [1,2,3], [1], [7,3,7], [3,1,4,2,3],[5,1,1,2,0,0]]:
        print(quick_sort(nums))
            
    