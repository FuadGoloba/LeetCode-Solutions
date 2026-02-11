"""
    Contains Duplicate II
    
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

    Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true
    
    Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true
    
    Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
"""

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    """
        Return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k using a hash map
        
        Intuition:
            - We only need to check for duplicates within a window of size k. We can use a hash map to store the the most recent index of each value in a hash map.
            - When we encounter a number, we check if it has been seen before and if the difference to its last occurrence is within k (i.e between the current index and the last index of that number is less than or equal to k. If it is, we return true. Otherwise, we update the last index of the current number in the hash map.)
            - If we finish iterating through the array without finding any duplicates within the specified distance, we return false.
            
        Steps:
            1. Initialize an empty hash map (window_map) to store the most recent index of each value in the array.
            2. Iterate through the array nums using a for loop with an index variable idx and a value variable num:
                - For each number num at index idx, check if num is already in the hash map (window_map):
                    - If num is in the hash map, check if the absolute difference between the current index (idx) and the last index of num (window_map[num]) is less than or equal to k:
                        - If the condition is satisfied, return true, as we have found two distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.
                - Update the hash map with the current index of num by setting window_map[num] = idx. This will ensure that we always have the most recent index of num in the hash map for future comparisons.
            3. If we finish iterating through the array without finding any duplicates within the specified distance, return false. 
            
        Time Complexity - O(n) : We are iterating through the array once, resulting in O(n) time complexity, where n is the length of the input array nums.
        Space Complexity - O(n) : In the worst case, we may store all elements of the array in the hash map if all elements are unique, resulting in O(n) space complexity, where n is the length of the input array nums.
    """
    
    window_map = {}
    
    for idx, num in enumerate(nums):
        if num in window_map and abs(window_map[num] - idx) <= k:
            return True
        window_map[num] = idx
    
    return False
    

def containsNearbyDuplicate2(nums: list[int], k: int) -> bool:
    """
        Return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k using a sliding window and hash set
        
        Intuition:
            The intuition is to use a sliding window technique and a hashset. We create a window, the size of k and find duplicates only within that window
            The hashset helps in storing elements and performing O(1) loookups and detecting elements within a window that already exists.
            Once we exceed traversal without finding duplicates in a window, we shift our window from the left by 1 and remove the left most element from the window hashset and try to find duplicates within the next window
            
        Steps: 
            1. Initialize an empty hash set (window_set) to store the unique elements within the current window.
            2. Initialize two pointers, l and r, to represent the left and right boundaries of the sliding window, starting at 0.
            3. Iterate through the array nums using a while loop with the condition r < len(nums):
                - Check if the size of the current window (r - l) exceeds k:
                    - If it does, remove the leftmost element (nums[l]) from the hash set (window_set) and move the left pointer (l) to the right by incrementing it by 1. This effectively shifts the window to the right.
                - Check if the current number (nums[r]) is already in the hash set (window_set):
                    - If it is, return true, as we have found two distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.
                - If nums[r] is not in the hash set, add it to the hash set (window_set) to keep track of the unique elements within the current window.
                - Move the right pointer (r) to the right by incrementing it by 1 to expand the window.
            4. If we finish iterating through the array without finding any duplicates within the specified distance, return false.
            
        Time Complexity - O(n) : We are iterating through the array once, resulting in O(n) time complexity, where n is the length of the input array nums.
        Space Complexity - O(k) : The hash set (window_set) will store at most k + 1 elements at any time (the size of the window), resulting in O(k) space complexity, where k is the input integer representing the maximum allowed distance between duplicate indices.   
    """
    window_set = set()
    l = 0
    r = 0

    while r < len(nums):
        # Check if we are still within the fixed window size; otherwise shift window and remove the left most element from window_set
        if (r - l) > k:
            window_set.remove(nums[l])
            l += 1
        
        if nums[r] in window_set:
            return True
        # Add values within the current window to the hash set if it doesn;t exist
        window_set.add(nums[r])
        r += 1
    return False

if __name__ == '__main__':
    for nums, k in [ ([1,2,3,1], 3), ([1,0,1,1], 1), ([1,2,3,1,2,3], 2) ]:
        print(containsNearbyDuplicate(nums, k))
        assert( containsNearbyDuplicate(nums, k) == containsNearbyDuplicate2(nums, k))