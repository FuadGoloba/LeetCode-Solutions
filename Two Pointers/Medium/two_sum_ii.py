"""
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.

    Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    
    Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
    
    Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
    
    SOLUTION:
    The intuition is to use two pointer technique. Two pointers l and r are initialised at both ends of the array respectively. 
    Since the array is sorted ascendingly, it reasons that the addition of values at respective positions of l and r when compared to teh target determines which pointer moves forward or backward.
    If the sum is greater than the target, them we need to reduce the next sum by moving r pointer backward (r - 1). And if lesser than target, we increase the next sum by moving l forward (l + 1)
    This is shifted till we arrive at pointers with values that equate to  the target. And then we can return the indices added by 1; [l + 1, r + 1]
"""

def twoSum(numbers: list[int], target: int) -> list[int]:
    """Return the indices of two numbers added by one as an integer array of length 2 such that the two numbers are equal to the given target

    Args:
        numbers (list[int]): 1-indexed array of integers sorted in non-decreasing order
        target (int): target number

    Returns:
        list[int]: array of length 2 with indices added by 1
    """
    l, r = 0, len(numbers) - 1

    while l < r:
        if (numbers[l] + numbers[r]) > target:
            r -= 1
        elif (numbers[l] + numbers[r]) < target:
            l += 1
        else:
            return [l + 1, r + 1]
        
if __name__ == '__main__':
    for numbers, target in [ ([2,7,11,15], 9), ([2,3,4], 6), ([-1,0], -1) ]:
        print(twoSum(numbers, target))