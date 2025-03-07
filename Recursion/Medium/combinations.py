"""
    Combinations
    
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]. You may return the answer in any order.
    
    Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    Explanation: There are 4 choose 2 = 6 total combinations.
    Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
   
    Example 2:
    Input: n = 1, k = 1
    Output: [[1]]
    Explanation: There is 1 choose 1 = 1 total combination.
    
    Constraints:
    1 <= n <= 20
    1 <= k <= n
"""

def combine(n: int, k: int) -> list[list[int]]:
    """
        Using Backtracking (DFS), Time = O(C(n,k)⋅k) where C(n,k) = n!/(k!(n-k)!), Space = O(C(n,k)⋅k)

        SOLUTION:
            The intuition is to use a backtracking approach (DFS) to explore every possible way to include or exclude a number in the combination.
            So for each number from [1....n]: we either include it in the current combination or we exclude it and move to the next and check that the current combination has k number of elemnts
            
            Steps:
                1. Building Combinations: We maintain a temporary list 'comb' which keeps track of the current combination being explored.
                    - Start with an empty combination: comb = []
                    - Start at index 1, and try to either include 1 or exclude it.
                    - If we include 1, move to the next number (index 2), and repeat the process.
                2. Base Case: When the combination reaches a size of k, we store it in all_combinations because it's a valid combination.
                    - Continue this process until a combination of size k is found. Once we reach a combination of size k, we add it to all_combinations.
                3. Backtracking: After trying the "include" option, we backtrack by removing the last added element (comb.pop()) and then try the "exclude" option.
                    - If we exclude 1, move to the next number without adding it to comb.
                    - Backtrack to explore other possible combinations.
    """
    all_combinations = []
    comb = []
    
    def backtrack(curr):
        # Base Case: We have a selected a combination of k numbers
        if len(comb) == k:
            all_combinations.append(comb.copy()) # Store the combination
            return
        
        for num in range(curr, n + 1): # Loop through numbers from the current point to n ensuring that we explore all possible combinations ate each step
            comb.append(num) # include a number from the range
            backtrack(num + 1) # move to the next number in order to add it to the combination skipping previously visited elemnts avoiding duplicates, e.g [1,2] is same comb as [2,1] but we skip [2,1] as 1 was previously visited before 2
            comb.pop() # Backtrack and remove last chosen number in order to explore other possibilities of numbers
        
    backtrack(1)
    return all_combinations

if __name__ == '__main__':
    for n, k in [(4, 2), (1, 1)]:
        print(combine(n, k))
        