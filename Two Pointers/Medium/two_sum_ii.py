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
"""

def twoSum(numbers: list[int], target: int) -> list[int]:
    """Return the indices of two numbers added by one as an integer array of length 2 such that the two numbers are equal to the given target
    
        Intuition:
            - Use two pointer technique. Two pointers l and r are initialised at both ends of the array respectively. 
            - Since the array is sorted ascendingly, it reasons that the addition of values at respective positions of l and r when compared to teh target determines which pointer moves forward or backward.
            - If the sum is greater than the target, them we need to reduce the next sum by moving r pointer backward (r - 1). And if lesser than target, we increase the next sum by moving l forward (l + 1)
            - This is shifted till we arrive at pointers with values that equate to  the target. And then we can return the indices added by 1; [l + 1, r + 1]
            
        Steps:
            1. Initialize two pointers, l and r, to the start and end of the array respectively.
            2. While l is less than r:
                - Calculate the sum of the values at the positions of l and r.
                - If the sum is greater than the target, move the r pointer backward (r - 1) to reduce the next sum.
                - If the sum is less than the target, move the l pointer forward (l + 1) to increase the next sum.
                - If the sum is equal to the target, return the indices of l and r added by one as an integer array [l + 1, r + 1].
            
        Time Complexity - O(n) : We traverse the array once with the two pointers, resulting in O(n) time complexity, where n is the length of the input array numbers.
        Space Complexity - O(1) : We use a constant amount of extra space for the two pointers.
    """
    l, r = 0, len(numbers) - 1

    while l < r:
        if (numbers[l] + numbers[r]) > target:
            r -= 1
        elif (numbers[l] + numbers[r]) < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return []

def twoSum2(numbers: list[int], target: int) -> list[int]:
    """
    Find two numbers in a sorted array that add up to a specific target using binary search.

    Args:
        numbers (list[int]): 1-indexed array of integers sorted in non-decreasing order
        target (int): target number

    Returns:
        list[int]: array of length 2 with indices added by 1
        
    Intuition:
        - Iterate through the array with a for loop. For each element, calculate the remainder by subtracting the current element from the target.
        - Use binary search to find the remainder in the remaining part of the array (from the next element to the end).
        - If the remainder is found, return the indices of the current element and the found element, both added by one.    
        
    Steps:
        1. Iterate through the array with a for loop, using index i to track the current element.
        2. For each element at index i, calculate the remainder by subtracting the current element from the target.
        3. Initialize two pointers, l and r, to the next element (i + 1) and the end of the array respectively.
        4. While l is less than or equal to r:
            - Calculate the mid index as the average of l and r.
            - If the element at mid index is equal to the remainder, return the indices of the current element and the found element, both added by one.
            - If the element at mid index is less than the remainder, move the l pointer forward (l + 1) to search in the right half of the array.
            - If the element at mid index is greater than the remainder, move the r pointer backward (r - 1) to search in the left half of the array.
        5. If the loop ends without finding the remainder, continue to the next iteration of the for loop until a solution is found (as guaranteed by the problem statement).   
        
    Time Complexity - O(n log n) : We iterate through the array once with a for loop (O(n)) and for each element, we perform a binary search (O(log n)), resulting in O(n log n) time complexity, where n is the length of the input array numbers.
    Space Complexity - O(1) : We use a constant amount of extra space for the pointers and variables used in the binary search. 
    
    Note: This approach is less efficient than the two-pointer technique (O(n)) due to the additional logarithmic factor from the binary search, but it still meets the requirement of using only constant extra space.
    """
    for i in range(len(numbers)):
        l, r = i + 1, len(numbers) - 1

        remainder = target - numbers[i]

        while  l <= r:
            mid = (l + r) // 2
            if numbers[mid] == remainder:
                return [i + 1, mid + 1]
            elif numbers[mid] < remainder:
                l = mid +  1
            else:
                r = mid -  1
    return []
        
if __name__ == '__main__':
    for numbers, target in [ ([2,7,11,15], 9), ([2,3,4], 6), ([-1,0], -1) ]:
        print(twoSum(numbers, target))