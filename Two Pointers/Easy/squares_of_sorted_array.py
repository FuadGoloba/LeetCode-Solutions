"""
    Squares of a sorted Array
    
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
    
    Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
    
    Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]
    
    Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.
    
    SOLUTION:
    The intuition is to use a a two pointer technique. Since the array is sorted in non-decreasing order, the largest absolute value will either be at the start or end of the array.
    Two pointers, (l and r) are used to compare the absolute values or squares at both ends(start and end of array).
    We initialise an output array (sorted_squares) the size of the provided array and place the largest squares starting from the last position
    After placing the largest square, we move the corresponding pointer inward (l += 1) for the left or (r -= 1) for the right
"""

def sortedSquares(nums: list[int]) -> list[int]:
    """Return the squares of a sorted array
    
    Time Complexity -> O(n)
    Space Complexity -> O(1)

    Args:
        nums (list[int]): integer array sorted in non-decreasing order

    Returns:
        list[int]: an array of the squares of each numver sorted in non-decreasing order
    """
    sorted_squares = [0] * len(nums)
    
    l, r = 0, len(nums) - 1 # Pointers at both ends of the array
    idx = len(nums) - 1 # pointer to track position or index of output
    
    while l <= r:
        # if abs(nums[l]) > abs(nums[r]):
        if (nums[l] ** 2) > (nums[r] ** 2):
            sorted_squares[idx] = nums[l] ** 2
            l += 1
        else:
            sorted_squares[idx] = nums[r] ** 2
            r -= 1
        idx -= 1
        
    return sorted_squares

if __name__ == '__main__':
    for nums in ( [-4,-1,0,3,10],  [-7,-3,2,3,11] ):
        print(sortedSquares(nums))
            