""" Merge Sorted Array

    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
    representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    
    Example 1:

    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    Example 2:

    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].
    Example 3:

    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

def merge(nums1, m, nums2, n):
    """
        Merge 2 sorted arrays using the Brute Force Approach. Modify nums1 in-place
        
        Intuition:
            - Create a copy of the first m elements of nums1 to avoid overwriting them during the merge process.
            - Use two pointers to iterate through the copied nums1 and nums2 arrays simultaneously, comparing elements and writing the smaller one back into nums1.
            - After one of the arrays is fully iterated, append any remaining elements from the other array to nums1.   
            
        Steps:
            1. Create a copy of the first m elements of nums1.
            2. Initialize two pointers, i and j, for iterating through the copied nums1 and nums2, and a pointer curr_idx for tracking the current index in nums1.
            3. While both pointers are within the bounds of their respective arrays:
                - Compare the elements at the current pointers.
                - Write the smaller element to nums1 at curr_idx and move the corresponding pointer and curr_idx forward.
            4. If there are remaining elements in either array, append them to nums1.

        Time Complexity - O(m + n) => O(n)
        Space Complexity - O(n)
        """
    # Create a copy of nums1
    nums1_copy = nums1[:m]
    i, j, curr_idx = 0, 0, 0

    # Merge the two arrays
    while i < m and j < n:
        if nums1_copy[i] < nums2[j]:
            nums1[curr_idx] = nums1_copy[i]
            i += 1
        else:
            nums1[curr_idx] = nums2[j]
            j += 1
        curr_idx += 1

    # If there are remaining elements in either array, append them
    if i < m:
        nums1[curr_idx:] = nums1_copy[i:]
    if j < n:
        nums1[curr_idx:] = nums2[j:]
        
def merge_optimal_1(nums1: list[int], m: int, nums2: list[int], n:int) -> None:
    """
        Merge 2 sorted arrays using Two Pointer Approach. Modify nums1 in-place
        
        Intuition:
            - Use two pointers to iterate through the two arrays from the end, comparing elements and writing the larger one back into nums1.
            - This approach avoids the need for extra space and allows us to fill nums1 from the end, ensuring that we do not overwrite any elements before they are compared.

        Steps:
            1. Initialize two pointers m and n, for iterating through nums1 and nums2 respectively, starting from the last valid elements.
            2. Use a third pointer curr_idx to track the current index in nums1.
            3. While there are elements in both arrays:
                - If nums1[m] > nums2[n], place nums1[m] at nums1[curr_idx] and move m and curr_idx backward.
                - Otherwise, place nums2[n] at nums1[curr_idx] and move n and curr_idx backward.
        4. If there are remaining elements in nums2, place them in nums1.
        
        Time Complexity - O(m + n) => O(n) : We iterate through both arrays once, resulting in O(m + n) time complexity, where m and n are the lengths of nums1 and nums2 respectively.
        Space Complexity - O(1) : We use a constant amount of extra space for the pointers.
    """
    curr_idx = len(nums1)

    while m > 0 and n > 0: # Iterate while there are elements in both arrays
        if nums1[m - 1] > nums2[n - 1]:
            nums1[curr_idx - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[curr_idx - 1] = nums2[n - 1]
            n -= 1
        
        curr_idx -= 1

    while n > 0: # If there are remaining elements in nums2, place them in nums1
        nums1[curr_idx - 1] = nums2[n - 1]
        n -= 1
        curr_idx -= 1
    

def merge_optimal_2(nums1: list[int], m: int, nums2: list[int], n:int) -> None:
    """Merge 2 sorted arrays using Two Pointer Approach. Modify nums1 in-place
    
        Intuition:
            - Use two pointers to iterate through the two arrays from the end, comparing elements and writing the larger one back into nums1.
            - This approach avoids the need for extra space and allows us to fill nums1 from the end, ensuring that we do not overwrite any elements before they are compared.
        
        Steps:
            1. Initialize two pointers, l and r, for iterating through nums1 and nums2 respectively, starting from the last valid elements.
            2. Use a third pointer idx to track the current index in nums1.
            3. While there are elements in nums2:
                - If nums1[l] > nums2[r], place nums1[l] at nums1[idx] and move l and idx backward.
                - Otherwise, place nums2[r] at nums1[idx] and move r and idx backward.
                
        Time Complexity - O(m + n) => O(n) : We iterate through both arrays once, resulting in O(m + n) time complexity, where m and n are the lengths of nums1 and nums2 respectively.
        Space Complexity - O(1) : We use a constant amount of extra space for the pointers.
    """
    l, r = m - 1, n - 1 # Start from the last valid elements of nums1 and nums2 respectively
    curr_idx = (m + n) - 1 # Start from the last index of nums1

    # Iterate while there are elements in nums2
    while r >= 0:
        # If nums has elements left and nums1[l] > nums2[r], place nums1[l] at nums1[idx]
        if l >= 0 and nums1[l] > nums2[r]:
            nums1[curr_idx] = nums1[l]
            l -= 1
        else:
            # Otherwise place nums2[r] at nums1[curr_idx]
            nums1[curr_idx] = nums2[r]
            r -= 1
        curr_idx -= 1

if __name__ == "__main__":
    for nums1, m, nums2, n,  in [ ([1,2,3,0,0,0], 3, [2,5,6], 3), ([1], 1, [], 0), ([0], 0, [1], 1) ]:
        merge_optimal_2(nums1, m, nums2, n)
        print(nums1)