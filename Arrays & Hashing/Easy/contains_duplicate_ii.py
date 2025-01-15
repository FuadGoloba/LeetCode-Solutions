"""
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
        Using a hashmap; Time = O(n), Memory = O(n)
        
        SOLUTION:
            The intuition is to use a hashmap to keep track of numbers traversed and their index. If a duplicate is encountered, we check if they are within the specified window size (i.e the difference between the indices of the duplicates is <= K)
            If it's <= K, then we know we have found duplicate values that are within the window otherwise we update that value in the hashmap with the latest index and continue searching for duplicates that meet the window.
    """
    
    window_map = {}
    
    for idx, num in enumerate(nums):
        if num in window_map and abs(window_map[num] - idx) <= k:
            return True
        window_map[num] = idx
    
    return False
    

def containsNearbyDuplicate2(nums: list[int], k: int) -> bool:
    """
        Using SLiding Window Technique and hashset, Time = O(n), Memory = O(n)
        
        SOLUTION:
            The intuition is to use a sliding window technique and a hashset. We create a window, the size of k and find duplicates only within that window
            The hashset helps in storing elements and performing O(1) loookups and detecting elements within a window that already exists.
            Once we exceed traversal without finding duplicates in a window, we shift our window from the left by 1 and remove the left most element from the window hashset and try to find duplicates within the next window
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