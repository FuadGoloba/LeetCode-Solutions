"""
    Trapping rain Water
    
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    
    Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

    Visual representation (Example 1):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]

        3            █
        2      █  ~~ █ █  ~  █
        1   █  █~~█~~█ █~~█~~█~~█
        0   █~~█~~█~~█~~█~~█~~█~~█
            0  1  2  3  4  5  6  7  8  9 10 11

        (█ = elevation bar, ~ = trapped water, total trapped = 6 units)

    Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

    Visual representation (Example 2):
        height = [4,2,0,3,2,5]

        5   █~~~~~~~~~~~~~~~~~~█
        4   █~~█~~~~~~~~~~~~~~~█
        3   █~~█~~~~~~█~~~~~~~~█
        2   █~~█~~~~~~█~~~~█~~~█
        1   █~~█~~~~~~█~~~~█~~~█
        0   █~~█~~█~~~█~~~~█~~~█
            0  1  2  3  4  5

        (█ = elevation bar, ~ = trapped water, total trapped = 9 units)

    Constraints:
    n == height.length
    0 <= height[i] <= 10^5
    1 <= n <= 2 * 10^4    
"""

def trap(height: list[int]) -> int:
    """
    Computes the amount of water that can be trapped after raining given an elevation map.
    
    Args:
        height (list[int]): A list of non-negative integers representing the elevation map.
    
    Returns:
        int: The total amount of trapped rainwater.
        
    Intuition:
        Use Dynamic Programming with arrays to store the maximum height to the left and right of each bar. 
        The water trapped above each bar is determined by the minimum of these two maximum heights minus the height of the bar itself.
    
    Time Complexity: O(n), where n is the number of bars in the elevation map. We traverse the height array three times (once for left max, once for right max, and once for calculating trapped water).
    Space Complexity: O(n), for the left_max_height and right_max_height arrays used to store the maximum heights to the left and right of each bar.

    Steps:
        1. Initialize two arrays, left_max_height and right_max_height, to store the maximum height to the left and right of each bar.
        2. Fill the left_max_height array by iterating from left to right, keeping track of the maximum height seen so far.
        3. Fill the right_max_height array by iterating from right to left, keeping track of the maximum height seen so far.
        4. Iterate through each bar and calculate the trapped water above it using the formula: min(left_max_height[i], right_max_height[i]) - height[i]. If this value is positive, add it to the total trapped water.
        5. Return the total trapped water after processing all bars.    

    """
    # Arr to store the max height on the left and right of each current bar to determine the bounds to trap water
    left_max_height = [0] * len(height)
    right_max_height = [0] * len(height)

    # calculate left max height
    left_max_height[0] = height[0] # first bar has itself as it's max left
    for l in range(1, len(height)):
        left_max_height[l] = max(left_max_height[l-1], height[l])

    # calculate right max height
    right_max_height[len(height) - 1] = height[len(height) - 1]
    for r in range(len(height) - 2, -1, -1):
        right_max_height[r] = max(right_max_height[r+1], height[r])

    # calculate the total unit trapped
    # i.e the min bound of the left most and right most height of the current bar will trap water without overflowing and the we also remove the height of the current bar which would also block water retention 
    total = 0
    for i in range(len(height)):
        trapped = min(left_max_height[i], right_max_height[i]) - height[i]
        if trapped > 0:
            total += trapped

    return total

def trap_optimized(height: list[int]) -> int:
    """
    Computes the amount of water that can be trapped after raining given an elevation map using a two-pointer approach.
    
    Args:
        height (list[int]): A list of non-negative integers representing the elevation map.
    
    Returns:
        int: The total amount of trapped rainwater.
        
    Intuition:
        Use two pointers to traverse the height array from both ends, keeping track of the maximum heights seen so far from both sides. 
        The water trapped above each bar is determined by the minimum of these two maximum heights minus the height of the bar itself.
    
    Time Complexity: O(n), where n is the number of bars in the elevation map. We traverse the height array once.
    Space Complexity: O(1), as we only use a constant amount of extra space for variables.

    Steps:
        1. Initialize two pointers, left and right, at the start and end of the height array, respectively.
        2. Initialize variables to keep track of the maximum heights seen so far from both sides (left_max and right_max).
        3. While left pointer is less than or equal to right pointer:
            - If left_max is less than right_max, calculate trapped water at left pointer and move left pointer to the right.
            - Otherwise, calculate trapped water at right pointer and move right pointer to the left.
        4. Return the total trapped water after processing all bars.    
    """
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total = 0

    while left <= right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total += right_max - height[right]
            right -= 1

    return total


if __name__ == "__main__":
    # Example usage
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))  # Output: 6
    print(trap_optimized(height))  # Output: 6

    height = [4,2,0,3,2,5]
    print(trap(height))  # Output: 9
    print(trap_optimized(height))  # Output: 9