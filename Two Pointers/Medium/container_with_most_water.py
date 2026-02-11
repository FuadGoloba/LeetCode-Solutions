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
        Return the maximum area of water a container can store using a brute force approach
        
        Intuition:
            - We can use a brute force approach to solve this problem by checking the area of water that can be contained between every pair of lines in the array. 
            - We can calculate the area for each pair of lines by taking the minimum height of the two lines and multiplying it by the distance between them (the difference in their indices). 
            - We can keep track of the maximum area found so far and return it at the end.
            - This approach has a time complexity of O(n^2) since we are checking every pair of lines, where n is the length of the input array height. 
            
        Steps:  
            1. Initialize a variable result to store the maximum area found, starting with 0.
            2. Use a nested loop to iterate through all pairs of lines in the array:
                - The outer loop will iterate through the array with an index left, starting from 0 to len(height) - 1.
                - The inner loop will iterate through the array with an index right, starting from left + 1 to len(height) - 1.
            3. For each pair of lines at indices left and right, calculate the area of water that can be contained between them using the formula: area = (right - left) * min(height[left], height[right]).
            4. Update the result variable with the maximum area found so far by comparing it with the current area calculated.
            5. After iterating through all pairs of lines, return the result variable, which contains the maximum area of water that can be stored in the container formed by the lines.    
            
        Time Complexity - O(n^2) : We are checking every pair of lines in the array, resulting in O(n^2) time complexity, where n is the length of the input array height.
        Space Complexity - O(1) : We are using a constant amount of extra space to store the result variable, regardless of the input size. 
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
        Return the maximum area of water a container can store using a two pointer approach
        
        Intuition:
            - We can use a two pointer technique to solve this problem more efficiently. 
            - We start with two pointers, left and right, at the beginning and end of the array respectively. 
            - We calculate the area of water that can be contained between the lines at the left and right pointers and update the maximum area found so far. 
            - We then move the pointer that has the smaller height inward, as moving the taller line inward will not increase the area, while moving the shorter line might lead to a larger area. 
            - We continue this process until the left and right pointers meet, at which point we will have found the maximum area of water that can be stored in the container formed by the lines.
        
        Steps:
            1. Initialize a variable result to store the maximum area found, starting with 0.
            2. Initialize two pointers, left and right, at the start and end of the array respectively.
            3. While left is less than right:
                - Calculate the area of water that can be contained between the lines at indices left and right using the formula: area = (right - left) * min(height[left], height[right]).
                - Update the result variable with the maximum area found so far by comparing it with the current area calculated.
                - Move the pointer that has the smaller height inward (i.e., if height[left] < height[right], move left pointer to left + 1; 
                otherwise, move right pointer to right - 1). This is because moving the taller line inward will not increase the area, while moving the shorter line might lead to a larger area.
            4. After the loop ends (when left and right pointers meet), return the result variable, which contains the maximum area of water that can be stored in the container formed by the lines.   
            
        Time Complexity - O(n) : We are traversing the array with two pointers, resulting in O(n) time complexity, where n is the length of the input array height.
        Space Complexity - O(1) : We are using a constant amount of extra space to store the result variable and the two pointers, regardless of the input size.
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