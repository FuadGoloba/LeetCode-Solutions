"""
    Rotate Array
    
    Given an array nums, rotate the array to the right by k steps, where k is non-negative.
    
    Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

    Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]              
    Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100] 

    Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105
"""

def rotate(nums: list[int], k: int) -> None:
    """
        Rotate the elements of the input list nums to the right by k steps in-place.         
        Do not return anything, modify nums in-place instead.

        Intuition:
            - We can use an auxiliary array to store the rotated version of the input array. 
            - We iterate through the input array and for each element, we calculate its new position in the rotated array using the formula (i + k) % len(nums), where i is the current index of the element in the input array.
            - After populating the auxiliary array with the rotated elements, we copy the elements back to the original input array nums.
            Note: we use the modulo operator to handle cases where k is greater than the length of the input array, 
                    ensuring that we wrap around to the beginning of the array when calculating the new positions. 
                    e.g., if k is 4 and the length of the input array is 3, then (i + k) % len(nums) will effectively rotate the array by 1 step to the right, as 4 % 3 is 1.
                            if k is 5 and the length of the input array is 3, then (i + k) % len(nums) will effectively rotate the array by 2 steps to the right, as 5 % 3 is 2.
                            if k is 4 and the length of the input array is 4, then (i + k) % len(nums) will effectively rotate the array by 0 steps to the right, as 4 % 4 is 0.

        Steps:
            1. Create an auxiliary array res of the same length as nums, initialized with zeros.
            2. Iterate through the input array nums using a for loop with index i.
            3. For each element at index i in nums, calculate its new position in the rotated array using the formula (i + k) % len(nums) and assign the value of nums[i] to res at the calculated position.
            4. After the loop, iterate through the auxiliary array res and copy each element back to the corresponding position in the original input array nums.
            5. The input array nums is now modified in-place to reflect the rotated version of the original array.
            6. The function does not return anything as the modification is done in-place.
            
        Time Complexity - O(n) : We iterate through the input array nums once to populate the auxiliary array res, and then we iterate through res to copy the elements back to nums. Both iterations are O(n), where n is the length of the input array nums.
        Space Complexity - O(n) : We use an auxiliary array res of the same length as nums to store the rotated version of the input array, resulting in O(n) space complexity.
    """
    res = [0] * len(nums)

    for i in range(len(nums)):
        res[(i + k) % len(nums)] = nums[i] # we calculate the new position for each element in nums and assign it to the corresponding position in res

    # After populating the auxiliary array res with the rotated elements, we copy the elements back to the original input array nums.
    for i in range(len(res)):
        nums[i] = res[i]
        
def rotate_inplace(nums: list[int], k: int) -> None:
    """
        Rotate the elements of the input list nums to the right by k steps in-place.         
        Do not return anything, modify nums in-place instead.

        Intuition:
            - We can use the reverse method to achieve the rotation in-place.
            - First, we reverse the entire array.
            - Then, we reverse the first k elements.
            - Finally, we reverse the remaining elements.

        Steps:
            1. Reverse the entire array.
            2. Reverse the first k elements.
            3. Reverse the remaining elements.
            
        Time Complexity - O(n) : We perform a constant number of passes over the array, each taking O(n) time.
        Space Complexity - O(1) : We perform the rotation in-place without using any extra space.
    """
    n = len(nums)
    k = k % n # Handle cases where k is greater than n

    # Reverse the entire array
    l, r = 0, n - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    # Reverse the first k elements
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    # Reverse the remaining elements
    l, r = k, n - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
        
def rotate_optimal(nums: list[int], k: int) -> None:
    """
        Rotate the elements of the input list nums to the right by k steps in-place.
        Do not return anything, modify nums in-place instead.

        Intuition:
            - We can use the reverse method to achieve the rotation in-place.
            - First, we reverse the entire array.
            - Then, we reverse the first k elements.
            - Finally, we reverse the remaining elements.
        Steps:
            1. Reverse the entire array.
            2. Reverse the first k elements.
            3. Reverse the remaining elements.
        Time Complexity - O(n) : We perform a constant number of passes over the array, each taking O(n) time.
        Space Complexity - O(1) : We perform the rotation in-place without using any extra space.
    """
    n = len(nums)
    k %= n  # Handle cases where k is greater than n
    # Helper function to reverse a portion of the array
    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    reverse(0, n - 1)  # Reverse the entire array
    reverse(0, k - 1)  # Reverse the first k elements
    reverse(k, n - 1)  # Reverse the remaining elements
    
if __name__ == "__main__":
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    rotate_optimal(nums1, k1)
    print(nums1)  # Output: [5,6,7,1,2,3,4]

    nums2 = [-1,-100,3,99]
    k2 = 2
    rotate_optimal(nums2, k2)
    print(nums2)  # Output: [3,99,-1,-100]