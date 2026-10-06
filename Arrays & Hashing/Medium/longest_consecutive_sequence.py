"""
    Longest Consecutive Sequence
    
    Given an array of integers nums, return the length of the longest consecutive elements sequence that can be formed from the elements in nums. 
    The consecutive elements sequence is a sequence of integers where each integer is one more than the previous integer.
    The elements do not have to be consecutive in the original array.

    You must write an algorithm that runs in O(n) time.
    
    Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    
    Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
    Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9.
    
    Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9    
"""

def longestConsecutive(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence in an array of integers.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The length of the longest consecutive elements sequence.
        
    Intuition:
        Use a set to store the unique elements of the array for O(1) lookups. 
        Iterate through the set and for each number, check if it's the start of a sequence (i.e., num - 1 is not in the set). 
           - E.g., if the number is 3, check if 2 is in the set. If 2 is not in the set, then 3 is the start of a sequence.
           - Then check for the next consecutive numbers (i.e., num + 1, num + 2, ...) and count how long the sequence is.
        
    Time Complexity: O(n), where n is the number of elements in the input array. Each element is processed at most twice (once for checking if it's the start of a sequence and once for counting the length of the sequence).
    Space Complexity: O(n), where n is the number of unique elements in the input array. The set is used to store the unique elements for O(1) lookups.
    Steps:
        1. Convert the input list to a set to eliminate duplicates and allow for O(1) lookups.
        2. Initialize a variable to keep track of the longest streak found.
        3. Iterate through each number in the set:
            - If the number is the start of a sequence (i.e., num - 1 is not in the set), initialize a current streak counter and check for consecutive numbers.
            - Increment the current streak counter for each consecutive number found.
            - Update the longest streak if the current streak is greater than the longest streak found so far.
        4. Return the length of the longest consecutive elements sequence found.    
    """
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only check for the start of a sequence
        if num - 1 not in num_set:
            current_num = num # Start of a new sequence
            current_streak = 1 # Initialize the current streak length

            # Continue to check for the next consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1 # Increment the current streak length

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1], 1),
        ([1, 2, 0, 1], 3),
        ([9,1,-3,2,4,8,3,-1,6,-2,-4,7], 4)
    ]

    for nums, expected in test_cases:
        result = longestConsecutive(nums)
        assert result == expected, f"Test failed for input {nums}. Expected {expected}, got {result}"
    print("All tests passed!") 