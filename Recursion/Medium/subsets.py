'''
Subsets {MEDIUM}
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''

def subsets(nums: list[int]) -> list[list[int]]:
    """
        Using Recursion, Time = O(2^n), Memory = O(2^n)
        
        SOLUTION:
            The intuition follows a recursive approach where you break down the problem step by step by removing the first element and solving for the rest.
            
            1. Base Case:
                - If nums is empty, return [[]], representing the empty subset. e.g subsets([]) => [[]]
            2. Recursive Step:
                - Compute the subsets of nums[1:] (all elements except the first). e.g subsets([1, 2]) => subsets([2]) => subsets([])
                - For each subset in subsets(nums[1:]): e.g subsets([2]) == [ subsets([]), [2] + subsets([]) ] == [ [], [2] ]
                    - Include it as is in the result of that subset i.e result == [ [] ]
                    - Create a new subset by adding nums[0] to its beginning i.e result == [ [], [2] + [] ] == [ [], [2] ]
            3. Merge Results:
                - Combine the subsets from the recursive call and the newly created subsets.
                - Return the final list of subsets.
    """
    
    if len(nums) == 0:
        return [[]]
    
    smaller_subsets = subsets(nums[1:])
    all_subsets = []
    
    for subset in smaller_subsets:
        all_subsets.append(subset)
        all_subsets.append([nums[0]] + subset)
        
    return all_subsets


def subsets2(nums: list[int]) -> list[list[int]]:
    '''
        Using DFS and Backtracking; Time = O(2n), Memory = O(n)
        
        SOLUTION:
            The intution is ti use depth first search with backtracking to explore all possible subsets. 
            Idea is to use a decision tree such that for each element in the array, we create a subset including an element and we create a susbet to not include that element and then build on that with the next elements
            
            Steps: 
                1. Recursive Exploration:
                    - Start with an empty subset and explore all possible subsets by making decisions at each step (include or exclude the current element).
                    - Recursively move to the next index after each decision.
                2. Backtracking Mechanism:
                    - Include nums[i] in subset, move forward, and explore further.
                    - Undo the inclusion (subset.pop()) to explore the alternative path (excluding nums[i]).
                    - This ensures that we explore both possibilities (including and excluding each element).
                3. Base Case (Stopping Condition):
                    - When i reaches len(nums), a valid subset is formed, so we add a copy to res and return.
    '''
    # In the array nums, at every step we have two choices for each element either we can ignore the element or we can include the element in our subset
    res = [] # Array to store all subsets
    subset = [] # array to store combinations
    
    # create a backtracking depth first search to make a decision on each element in the array
    def dfs(i):
        # base case - if there's no element to make a decision on , we append current susbset to the result and exit the function
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        # Include the current number in the subset and recurse on the next element in the array
        subset.append(nums[i])
        dfs(i + 1)
        
        # To NOT include the current number in the subset and recurse on the next element in the array
        subset.pop()
        dfs(i + 1)
    
    dfs(0) # call the dfs function to start on the first item
    return res
    
if __name__ == '__main__':
    for nums in [[1,2,3], [1], [0,1,3,4,5,6]]:
        print(subsets2(nums))
        assert sorted(subsets(nums)) == sorted(subsets2(nums))
            
                
            
            