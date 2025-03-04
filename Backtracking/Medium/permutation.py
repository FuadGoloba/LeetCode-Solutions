''' PERMUTATIONS {MEDIUM}

    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

    Example 3:
    Input: nums = [1]
    Output: [[1]]
'''

def permute(nums: list[int]) -> list[list[int]]:
    """
        Using Recursion; Time = O(n! * n) == O(n!), Space = O(n!)
        
        SOLUTION:
            The intuition is to use a recursive approach to generate all permutations of the given list by inserting the first element of nums into all positions of permutations of the remaining elements.
            The core idea is to take one element at a time (in this case, the first element nums[0]), recursively find the permutations of the rest of the list, and then insert the current element at all possible positions in those permutations.
            Steps:
                1. Base Case:
                    If nums is empty (len(nums) == 0), return [[]] (a list with an empty list).
                    This ensures that when we start inserting elements, we have something to build on.
                2. Recursive Step:
                    You start by recursively computing all permutations of the sublist nums[1:], i.e., the list excluding the first element (nums[0]).
                    Then, you take the permutations of nums[1:] and insert nums[0] into each possible position of those permutations.
                3. Return all generated permutations.
                
            Example: nums = [1,2,3]
            1. Recursive Call 1: permute([1,2,3])
                nums[0] = 1
                Recursively call permute([2,3])
            2. Recursive Call 2: permute([2,3])
                nums[0] = 2
                Recursively call permute([3])
            3. Recursive Call 3: permute([3])
                nums[0] = 3
                Recursively call permute([])
            4. Base Case: permute([]) → [[]]
                Now, start returning upwards.
                
            Building Up Permutations
            Step 1: Returning from permute([3])
                Current nums[0] = 3
                curr_perms = [[]] (from base case)
                Insert 3 at all positions in [] → [[3]]
            Step 2: Returning from permute([2,3])
                Current nums[0] = 2
                curr_perms = [[3]] (from previous step)
                Insert 2 at all positions in [3]
                Insert at index 0: [2,3]
                Insert at index 1: [3,2]
                all_permutations = [[2,3], [3,2]]
            Step 3: Returning from permute([1,2,3])
                Current nums[0] = 1
                curr_perms = [[2,3], [3,2]]
                Insert 1 at all positions:

                For [2,3]:
                Insert at index 0: [1,2,3]
                Insert at index 1: [2,1,3]
                Insert at index 2: [2,3,1]
                
                For [3,2]:
                Insert at index 0: [1,3,2]
                Insert at index 1: [3,1,2]
                Insert at index 2: [3,2,1]
            Final Result:
                [[1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1]]    
    """
    
    # Base case
    if len(nums) == 0:
        return [[]]
    
    curr_perms: list[list] = permute(nums[1:])
    all_permutations: list[list[int]] = []
    
    for perm in curr_perms:
        for i in range(len(perm) + 1):
            perm_copy = perm.copy()
            perm_copy.insert(i, nums[0])
            all_permutations.append(perm_copy)
            
    return all_permutations


def permute1(nums):
    
    '''
        Using Backtracking Recursion approach to divide the problem into sub problems and permute each sub problem till we reach a base case 
        - Base case - an array of 1 item would return itself (i.e permute([1]) will return [[1]] )
        - if not base case we want to divide the problem into subproblems by looping through the array and popping the first item and recuresively permuting the rest of the array
            till we get to the base case, and then work our way back up to the main problem by including the popped item to the permutation result of the sub problems
        - 
        Time = O(n), Memory = O(n)
    '''
    
    res = [] # Initialise an array to store the result
    
    # base case - an array of 1 item would return itself (i.e permute([1]) will return [[1]] )
    if len(nums) == 1:
        return [nums[:]] # Return a deep copy of the array so we don't affect the original array
    
    # Dividing the problem into subproblems 
    for i in range(len(nums)): # Loop through the array popping the first item and recursively permuting the rest of the array (e.g [1,2,3] will be divided into sub problems [2,3], [3, 1], [1, 2])
        popped = nums.pop(0)
        permutations = permute(nums) # (e.g sub problem [2, 3] will also reduce to sub problems [3], and [2] where we we have reached our base case and sub[3] will return [[3]] as the result of the permutation of [3], and sub[2] returns [[2]])
        
        # Once we get the permutations of any problem, we want to append the popped item to the permutations which gives us the permutations for the current problem.
                # (e.g for sub[2,3] of which we first popped item 2 from the array and returned permute of [3] as [[3]]; one of its permutation result will be [[3,2]] as we appended the poppped item back)
        for perm in permutations:
            perm.append(popped)
            
        res.extend(permutations) # including all permutation results of sub problems to the final result
            
        # We also want to append the popped item back to the original array and continue our loop till we have permuted the entire main problem
                # (e.g for our sub problem [2,3], which we first removed the first item reducing the array to [3], now we append the removed item back to the original array i.e [3,2] so our initial loop can continue by removing first item - 3 and permuting [2] to return [[2]] 
                    # and then appending back to return permutation result [[2, 3]] which is the 2nd permutation result of subproblem [2, 3])
        nums.append(popped)
        
    return res # Return the final result

if __name__ == '__main__':
    import math
    for nums in [ [1,2,3], [0,1], [1] ]:
        print(permute1(nums))
        assert sorted(permute(nums)) == sorted(permute1(nums))
        assert len(permute(nums)) == math.factorial(len(nums))