"""Container with most water

    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store. # Notice that you may not slant the container.

    Example 1
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

    Example 2:
    Input: height = [1,1]
    Output: 1

    SOLUTION:
    The intuition is to use a two pointer technique. Two pointers (l, r) are initialised at both ends of the array. The technique starts with the widest container and moves the pointers inward based on the comparison of heights.
    Increasing the width of the container can only lead to a larger area if the height of the new boundary is greater. By moving the pointers towards the center, we explore containers with the potential for greater areas.
    The area is computed by the multiplication of the width and minimum height, ie (r - l) * min(height[l], height[r])
"""

def maxArea1(height):
    '''
        Brute Force solution: Time = O(n2)
    '''
    result = 0 # Initialise our result to be 0
    
    # Traverse the array; calculating the area of each element across the next elements in the array and updating the result with the maximum area
    for left in range(len(height)):
        for right in range(left + 1, len(height)):
            area = (right - left) * min(height[left], height[right]) # The area is the width of the container (x-axis) multiplied by the minimum height. (i.e the height that can hold water without pouring)
            result = max(area, result)
    return result


def maxArea2(height):
    '''
        Using a Greedy Two Pointer approach to calculate the max area by only shifting the pointer unless we find a better solution: Time = O(n)
    '''
    result = 0
    left, right = 0, len(height) - 1 # Initialise two pointers at the start and end of the array;
    
    # Starting from opposite ends of the array/container, check that we haven't shifted our pointers to be equal to one another
    while left < right:
        area = (right - left) * min(height[left], height[right]) # Compute the area
        result = max(area, result) # Update the area if there exists a better solution
        
        # Move the pointers inward to the center by shifting the pointer that has the minimum height to its adjacent position (either left or right depending on which is minimum)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return result

if __name__ == '__main__':
    for height in [[1,8,6,2,5,4,8,3,7], [1,1], [1,2,1]]:
        print(maxArea2(height))