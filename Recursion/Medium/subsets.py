# Subsets {MEDIUM}
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

def subsets(nums):
    
    '''
        Idea is to use a decision tree such that for each element in the array, we create a subset including the element and we create a susbet to not include 
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
    for nums in [[1,2,3], [1]]:
        print(subsets(nums))
            
                
            
            