"""
    Missing Element in Sorted Array
    
    Given an integer array nums which is sorted in ascending order and all of its elements are unique, and given an integer k.
    Return the kth missing element in this array.

    
    Example 1:
    Input: nums = [4,7,9,10], k = 1
    Output: 5
    Explanation: The first missing element is 5.    
    
    Example 2:
    Input: nums = [4,7,9,10], k = 3
    Output: 8
    Explanation: The missing elements are [5,6,8,...], hence the third missing element is 8.
    
    Example 3:
    Input: nums = [1,2,4], k = 3
    Output: 6
    Explanation: The missing elements are [3,5,6,7,...], hence the third missing element is 6.
    

    Constraints:
    1 <= nums.length <= 5 * 104
    1 <= nums[i] <= 107
    nums is sorted in ascending order, and all the elements are unique.
    1 <= k <= 108
"""

def missingElement(nums: list[int], k: int) -> int:
    """Return the kth missing element in the sorted array using Two Pointers.

    Intuition:
    The number of missing elements between two numbers is the difference between the two numbers minus one.
     - If the number of missing elements is greater than or equal to k, then the kth missing element is in the range between the two numbers.
     - If the number of missing elements is less than k, then the kth missing element is not in the range between the two numbers, 
       and we can move the left pointer to the right and subtract the number of missing elements from k to find the new k.
    - If we reach the end of the array without finding the kth missing element, then the kth missing element is greater than the last element in the array, and we can return the last element plus k.
    
    Steps:
    1. Initialize two pointers, l and r, to the first and second elements of the array, respectively.
    2. While r is less than the length of the array:
        a. Calculate the number of missing elements between nums[l] and nums[r] as missing = nums[r] - nums[l] - 1.
        b. If missing is greater than or equal to k, then the kth missing element is in the range between nums[l] and nums[r], and we can return nums[l] + k.
        c. If missing is less than k, then the kth missing element is not in the range between nums[l] and nums[r], and we can move the left pointer to the right and subtract missing from k to find the new k.
        d. Move the left pointer to the right and the right pointer to the right.
    3. If we reach the end of the array without finding the kth missing element, then the kth missing element is greater than the last element in the array, and we can return nums[l] + k.

    Time complexity: O(n) in the worst case, where n is the length of the array, if k is greater than the number of missing elements in the array. Otherwise, it is O(1).
    Space complexity: O(1) since we are using only a constant amount of extra space
    """
    l, r = 0, 1

    while r < len(nums):
        missing = nums[r] - nums[l] - 1
        if missing >= k: # kth number lies in the missing range
            return nums[l] + k
        else: # kth number is not in the missing range so we can move the left pointer to the right and subtract the number of missing elements from k to find the new k
            k -= missing
        l += 1
        r += 1
    # Should the loop finish without an answer, kth missing number exists outside the element
    return nums[l] + k

def missingElementBinarySearch(nums: list[int], k: int) -> int:
    """Return the kth missing element in the sorted array using binary search.

    Intuition:
    We can use binary search to find the kth missing element in the sorted array. 
    The number of missing elements between nums[0] and nums[mid] is nums[mid] - nums[0] - mid. 
     - If the number of missing elements is greater than or equal to k, then the kth missing element is in the range between nums[0] and nums[mid], and we can move the right pointer to mid.
     - If the number of missing elements is less than k, then the kth missing element is not in the range between nums[0] and nums[mid], and we can move the left pointer to mid + 1 and subtract the number of missing elements from k to find the new k.
    - If we reach the end of the array without finding the kth missing element, then the kth missing element is greater than the last element in the array, and we can return the last element plus k.

    Steps:
    1. Initialize two pointers, l and r, to the first and last elements of the array, respectively.
    2. While l is less than or equal to r:
        a. Calculate the middle index as mid = (l + r) // 2.
        b. Calculate the number of missing elements between nums[0] and nums[mid] as missing = nums[mid] - nums[0] - mid.
        c. If missing is greater than or equal to k, then the kth missing element is in the range between nums[0] and nums[mid], and we can move the right pointer to mid - 1.
        d. If missing is less than k, then the kth missing element is not in the range between nums[0] and nums[mid], and we can move the left pointer to mid + 1 and subtract missing from k to find the new k.
    3. If we reach the end of the array without finding the kth missing element, then the kth missing element is greater than the last element in the array, and we can return nums[r] + k - (nums[r] - nums[0] - r) which is the last element plus k minus the number of missing elements between nums[0] and nums[r].

    Time complexity: O(log n) where n is the length of the array since we are using binary search.
    Space complexity: O(1) since we are using only a constant amount of extra space
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        missing = nums[mid] - nums[0] - mid # number of missing elements between nums[0] and nums[mid]
        if missing >= k: # kth number lies in the missing range
            r = mid - 1
        else: # kth number is not in the missing range so we can move the left pointer to mid + 1 and subtract the number of missing elements from k to find the new k
            l = mid + 1

    return nums[r] + k - (nums[r] - nums[0] - r) # kth missing number exists outside the element, so we can return the last element plus k minus the number of missing elements between nums[0] and nums[r]

if __name__ == "__main__": 
    print(missingElement([4,7,9,10], 1)) # 5
    print(missingElement([4,7,9,10], 3)) # 8
    print(missingElement([1,2,4], 3)) # 6
    
    print(missingElementBinarySearch([4,7,9,10], 1)) # 5
    print(missingElementBinarySearch([4,7,9,10], 3)) # 8
    print(missingElementBinarySearch([1,2,4], 3)) # 6

    assert missingElement([4,7,9,10], 1) == missingElementBinarySearch([4,7,9,10], 1)
    assert missingElement([4,7,9,10], 3) == missingElementBinarySearch([4,7,9,10], 3)
    assert missingElement([1,2,4], 3) == missingElementBinarySearch([1,2,4], 3)