""" 3Sum Problem

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

    Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2]. Notice that the order of the output and the order of the triplets does not matter.

    Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

    Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
"""

def threeSum1(nums):
    '''
        Return all unique triplets in the array which gives the sum of zero using HashSet; 
        
        Intuition:
        - Sort the input array to handle duplicates easily.
        - Fix one element and use a hash set to find pairs that sum to the negative of the fixed element.
        - This is similar to the Two-Sum problem, but we need to ensure that we are not using the same element twice and that we are not adding duplicate triplets to the result.   

        Steps:
        1. Sort the input array to handle duplicates easily.
        2. Initialize a set to store unique triplets.
        3. Iterate through the sorted array, fixing one element at a time.
        4. For each fixed element, use a hash set to find pairs of numbers that sum to the negative of the fixed element.
        5. If a valid pair is found, add the triplet (fixed element, pair elements) to the result set.
        6. Convert the set of triplets to a list of lists and return it.    
        
        Time Complexity - O(n^2) : We have an outer loop that iterates through the array and an inner loop that also iterates through the array, resulting in O(n^2) time complexity.
        Space Complexity - O(n) : In the worst case, we may store all unique triplets in the result set, which can take up to O(n) space. Additionally, the hash set used for finding pairs can also take up to O(n) space in the worst case.   
    '''
    nums.sort()  # Sort the input to avoid duplicates easily
    result = set()  # Use a set to store unique triplets

     # Fix one of the numbers of the triplets and treat the rest of the solution as a Two-Sum (i.e Fix x and apply twosum on y and z)
    # Traverse the list, fixing each element
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first element
            continue
        
        target = -nums[i]
        hashset = set()
        
        for j in range(i + 1, len(nums)):
            remainder = target - nums[j]
            if remainder in hashset:
                result.add((nums[i], nums[j], remainder))  # Add as a tuple
            else:
                hashset.add(nums[j])
    
    return [list(triplet) for triplet in result]  # Convert set of tuples to list of lists


def threeSum2_optimal(nums):
    '''
        Return all unique triplets in the array which gives the sum of zero using Two Pointers;
        
        Intuition:
        - Sort the input array to handle duplicates easily.
        - Fix one element and use two pointers to find pairs that sum to the negative of the fixed element.
        - This is similar to the Two-Sum problem, but we need to ensure that we are not using the same element twice and that we are not adding duplicate triplets to the result.   
        
        Steps:
        1. Sort the input array to handle duplicates easily.
        2. Initialize a list to store unique triplets.
        3. Iterate through the sorted array, fixing one element at a time.
        4. For each fixed element, use two pointers (left and right) to find pairs of numbers that sum to the negative of the fixed element.
        5. If a valid pair is found, add the triplet (fixed element, pair elements) to the result list. 
        6. Move the left pointer forward and skip duplicates, and move the right pointer backward and skip duplicates to avoid adding duplicate triplets to the result.
        7. Return the result list.      
        
        Time Complexity - O(n^2) : We have an outer loop that iterates through the array and an inner loop that uses two pointers to iterate through the array, resulting in O(n^2) time complexity.
        Space Complexity - O(1) : We use a constant amount of extra space for the two pointers and the result list does not count towards extra space since it is used to store the output
    '''

    result = [] # Result list to store 3sum
    nums.sort() # Sort list in ascending order to keep duplicates adjacent to one another
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]: # Check that we don't fix an element that has been fixed previously (Skip duplicate element)
            continue
        
        #### Now we have a Two Sum solution
        # Initialise left and right pointers
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        
        # Run a loop until left pointer is less than right if the sum of triplets equal 0 and append to the result
        while left < right:
            if nums[left] + nums[right] < target: # If the sum is less then the target, then we move the left pointer to the next element; thus increasing the sum since the array is sorted
                left += 1
            elif nums[left] + nums[right] > target: # If the sum is greater then the target, then we move the right pointer to the lement before; thus reducing the sum 
                right -= 1
            
            # Here we get the three sum and we append the elements into the result and shift the left pointer to the next adjacent element   
            else:
                result.append([nums[i], nums[left], nums[right]])   
                left += 1
                
                # After we have found a triplet, we need to skip any duplicate values for the left pointer to avoid adding duplicate triplets to the result. 
                while nums[left] == nums[left - 1] and left < right: # if duplcate value of left pointer, we skip and shift the left pointer forward
                    left += 1     
    return result


def threeSum3(nums: list[int]) -> list[list[int]]:
    """ Return all unique triplets in the array which gives the sum of zero using HashSet with categorization of numbers;
    
        Intuition:  
        Categorize the numbers
        - Separate the numbers in the array into three lists: positives, negatives, and zeros.
        
        Handle Triplets with Zeros:
        - If there are at least three zeros, include [0,0,0] in the result since their sum is zero.
        - For combinations involving one zero, find pairs of numbers (one positive and one negative) that sum to zero.
        
        Handle one zero and a pair of positives or negatives:
        - If there is at least one zero, for each negative number, check if its positive counterpart exists in the positive list. 
        If it does, add the triplet (negative, 0, positive) to the result set.

        Handle Non-Zero Triplets:
        - Iterate through all unique pairs of numbers from the negative and positive lists.
        - Check if the complement of their sum (e.g., -(a + b)) exists in the appropriate list.
        - E.g, negative = [-1, -1, -4], positive = [1, 2, 3], therefore -(-1 + -1) exsts in positive; we have a triplet [-1, -1, 2]
        
        Avoid Duplicates:
        - Use a set to store results, which avoids duplicate triplets naturally. 
        
        Steps:
        1. Initialize a set to store unique triplets.
        2. Separate the numbers in the array into three lists: positives, negatives, and zeros.
        3. If there are at least three zeros, add the triplet (0, 0, 0) to the result set.
        4. For each negative number, check if its positive counterpart exists in the positive list. If it does, add the triplet (negative, 0, positive) to the result set.
        5. Iterate through all unique pairs of negative numbers and check if their complement (the negative of their sum) exists in the positive list. If it does, add the triplet (negative1, negative2, complement) to the result set.
        6. Iterate through all unique pairs of positive numbers and check if their complement (the negative of their sum) exists in the negative list. If it does, add the triplet (positive1, positive2, complement) to the result set.
        7. Convert the set of triplets to a list of lists and return it.        
        
        Time Complexity - O(n^2) : We have nested loops that iterate through the negative and positive lists to find pairs, resulting in O(n^2) time complexity.
        Space Complexity - O(n) : We use additional space to store the categorized lists (posit and negatives) and the result set, which can take up to O(n) space in the worst case.  

    """
    result = set()

    # Categorize numbers
    pos, neg, zero = [], [], []

    for num in nums:
        if num == 0:
            zero.append(num)
        elif num < 0:
            neg.append(num)
        else:
            pos.append(num)
            
    # Create sets for easy lookup
    N, P, = set(neg), set(pos)

    # Handle Zero Triplets
    if len(zero) >= 3:
        result.add( (0, 0, 0) )

    # Handle Pair with a Zero
    if zero:
        for n in N:
            if -n in P:
                result.add((-n, 0, n))

    # Handle Non Zero Triplets for positives and negatives using complements of one category on another
    for i in range(len(neg)):
        for j in range(i + 1, len(neg)):
            target = -(neg[i] + neg[j])
            if target in P:
                result.add( tuple(sorted([neg[i], neg[j], target])) )

    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            target = -(pos[i] + pos[j])
            if target in N:
                result.add( tuple(sorted([pos[i], pos[j], target])) )

    return list(result)
    

if __name__ == '__main__':
    for nums in [[-1,0,1,2,-1,-4], [0,1,1],[0,0,0]]:
        print(threeSum3(nums))
    
        