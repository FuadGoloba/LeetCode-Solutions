"""
    Minimum Size Subarray Sum
    
    Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
    of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
    
    Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    
    
    Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1
    Explanation: The subarray [4] has the minimal length under the problem constraint.

    Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0
    Explanation: There is no subarray with a sum greater than or equal to 11.

    Constraints:
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104
    
    Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

def minSubArrayLen(target: int, nums: list[int]) -> int:
    """
        Return the minimal length of a contiguous subarray of which the sum is greater than or equal to target using a sliding window technique
        
        Intuition:
            - We can use a sliding window technique to find the minimal length of a contiguous subarray that meets the condition. 
            - We will maintain a window that expands to the right until the sum of the elements in the window is greater than or equal to the target. 
            - Once we have a valid window, we will try to shrink it from the left to find the minimal length.
            
        Steps:
            1. Initialize two pointers, window_start and window_end, to represent the current window. Set window_start = 0 and window_end = 0.
            2. Initialize a variable current_sum to keep track of the sum of the elements in the current window. Set current_sum = 0.
            3. Initialize a variable min_length to store the minimum length of a valid subarray found so far. Set min_length = float('inf') (or the length of the input array + 1) to represent an initially infinite length.
            4. Iterate through the array nums using a while loop with window_end as the loop variable:
                - Add nums[window_end] to current_sum to include the current element in the window.
                - While current_sum is greater than or equal to target:
                    - Update min_length with the smaller value between min_length and the current window size (window_end - window_start + 1).
                    - Subtract nums[window_start] from current_sum to shrink the window from the left.
                    - Increment window_start by 1 to move the left pointer to the right.
                - Increment window_end by 1 to expand the window to include the next element.
            5. After the loop, check if min_length is still float('inf'). If it is, it means we did not find any valid subarray, so return 0. Otherwise, return min_length as the result.
            
        Time Complexity - O(n) : We are iterating through the array once with the right pointer, and in the worst case, the left pointer also iterates through the array, resulting in O(n) time complexity, where n is the length of the input array nums.
        Space Complexity - O(1) : We are using a constant amount of space for the pointers and the current_sum variable, resulting in O(1) space complexity.
    """
    window_start, window_end = 0, 0
    total_window = 0
    min_length = len(nums) + 1

    # Expand the window to the right until we find a valid window that meets the condition (total_window >= target). Once we have a valid window, we will try to shrink it from the left to find the minimal length.
    while window_end < len(nums):
        total_window += nums[window_end] # Expand the window to the right by adding the current element to total_window
        while total_window >= target: # Check if the current window meets the condition (total_window >= target)
            min_length = min((window_end - window_start) + 1, min_length)
            total_window -= nums[window_start] # Shrink the window from the left by subtracting the leftmost element from total_window
            window_start += 1
        window_end += 1
        
    return 0 if min_length > len(nums) else min_length # If min_length is still greater than the length of the input array, it means we did not find any valid subarray, so we return 0. Otherwise, we return min_length as the result.

def minSubArrayLen2(target: int, nums: list[int]) -> int:
    """
        Return the minimal length of a contiguous subarray of which the sum is greater than or equal to target using a sliding window technique with a for loop
        
        Intuition:
            - Similar to the previous solution, we can use a sliding window technique to find the minimal length of a contiguous subarray that meets the condition. 
            - We will maintain a window that expands to the right until the sum of the elements in the window is greater than or equal to the target. 
            - Once we have a valid window, we will try to shrink it from the left to find the minimal length.
            
        Steps:
            1. Initialize two pointers, window_start and window_end, to represent the current window. Set window_start = 0 and window_end = 0.
            2. Initialize a variable current_sum to keep track of the sum of the elements in the current window. Set current_sum = 0.
            3. Initialize a variable min_length to store the minimum length of a valid subarray found so far. Set min_length = float('inf') (or the length of the input array + 1) to represent an initially infinite length.
            4. Iterate through the array nums using a for loop with an index variable i:
                - Add nums[i] to current_sum to include the current element in the window.
                - While current_sum is greater than or equal to target:
                    - Update min_length with the smaller value between min_length and the current window size (i - window_start + 1).
                    - Subtract nums[window_start] from current_sum to shrink the window from the left.
                    - Increment window_start by 1 to move the left pointer to the right.
            5. After the loop, check if min_length is still float('inf'). If it is, it means we did not find any valid subarray, so return 0. Otherwise, return min_length as the result.
    """
    window_start = 0
    current_sum = 0
    min_length = float('inf')

    for i in range(len(nums)):
        current_sum += nums[i]
        while current_sum >= target:
            min_length = min(min_length, i - window_start + 1)
            current_sum -= nums[window_start]
            window_start += 1

    return 0 if min_length == float('inf') else min_length

def minSubArrayLenFollowUp(target: int, nums: list[int]) -> int:
    """
        Return the minimal length of a contiguous subarray of which the sum is greater than or equal to target using a binary search technique
        
        Intuition:
            - We can use a binary search technique to find the minimal length of a contiguous subarray that meets the condition. 
            - We will first calculate the prefix sums of the input array nums, which will allow us to quickly calculate the sum of any subarray. 
            - Then, we will iterate through the prefix sums and use binary search to find the smallest index j such that prefix_sums[j] - prefix_sums[i] >= target, where i is the current index in the iteration.
            
        Steps:
            1. Calculate the prefix sums of the input array nums and store them in an array prefix_sums. The prefix sum at index i will be the sum of all elements from index 0 to index i in the input array.
            2. Initialize a variable min_length to store the minimum length of a valid subarray found so far. Set min_length = float('inf') (or the length of the input array + 1) to represent an initially infinite length.
            3. Iterate through the prefix sums using a for loop with an index variable i:
                - Use binary search to find the smallest index j such that prefix_sums[j] - prefix_sums[i] >= target.
                - If such an index j is found, update min_length with the smaller value between min_length and (j - i).
            4. After the loop, check if min_length is still float('inf'). If it is, it means we did not find any valid subarray, so return 0. Otherwise, return min_length as the result.
            
        Time Complexity - O(n log(n)) : We are iterating through the prefix sums once, which takes O(n) time, and for each prefix sum, we are performing a binary search, which takes O(log(n)) time. Therefore, the overall time complexity is O(n log(n)).
        Space Complexity - O(n) : We are using an additional array to store the prefix sums, which takes O(n) space, where n is the length of the input array nums.
        Note: This solution is less efficient than the O(n) sliding window solution, but it demonstrates an alternative approach using binary search.
    """
    # Calculate prefix sums
    prefix_sums = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

    min_length = float('inf')
    # Iterate through the prefix sums and use binary search to find the smallest index j such that prefix_sums[j] - prefix_sums[i] >= target
    for i in range(len(prefix_sums)):
        target_sum = prefix_sums[i] + target # We want to find the smallest index j such that prefix_sums[j] >= target_sum
        left, right = i, len(prefix_sums) - 1
        while left <= right: # Binary search to find the smallest index j such that prefix_sums[j] >= target_sum
            mid = left + (right - left) // 2
            if prefix_sums[mid] >= target_sum:
                min_length = min(min_length, mid - i)
                right = mid - 1
            else:
                left = mid + 1

    return 0 if min_length == float('inf') else min_length


if __name__ == "__main__":
    for target, nums in [ (7, [2,3,1,2,4,3]), (4, [1,4,4]), (11, [1,1,1,1,1,1,1,1]) ]:
        print(minSubArrayLen(target, nums)) # Output: 2, 1, 0
        print(minSubArrayLen2(target, nums)) # Output: 2, 1, 0
        print(minSubArrayLenFollowUp(target, nums)) # Output: 2, 1, 0
        