"""Climbing stairs

    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""

def climbStairs1(n):
    '''
        Using Recursion (DFS) with memoization using a hashmap, Time = O(n), Memory = O(n)
        
        SOLUTION
        To calculate the number of ways to climb the stairs, we can observe that when we are on the nth stair, we have 2 options:
            1. Either we climb one stair from the (n - 1)th stair or
            2. We climb two stairs from the (n - 2)th stair
        We can therefore recursively solve this problem similarly to the concept of Fibonacci series. But we store computed results in a hashmap tp avoid re-computations
    '''
    hashmap = {0:1, 1:1}
    def fib(n):
        if n in hashmap:
            return hashmap[n]
        
        hashmap[n] = fib(n-1) + fib(n - 2)
        return hashmap[n]
    
    # returns the count of ways to climb to the top
    return fib(n)

def climbStairs2(n):
    '''
        Using Dynamic Programming concept with Memoization to avoid computing repeated solutions
        - Uses Bottom up dp approach
            - ceate an array dp and initialise with None to represent a subproblem not solved
            - Only call the recursive method if the sub problem is not solved (i.e None)
        Time = O(n), Memory = O(n)
    '''
    # breaking the whole problem into subproblems and solving each subproblem
    def fib(n, dp):
        # UNlike the usual fibonacci sequence where we return 0 if n is 0; here we return 1 since the number of ways to reach nth step is fib(n + 1)
        if n <= 1:
            return 1
        
        # Check if the sub problem has been solved and return the solution
        if dp[n] != None:
            return dp[n]
        
        # compute solutions for subproblems up until n
        dp[n] = fib(n-1, dp) + fib(n - 2, dp)
        
        return dp[n] # returns the solution of the whole problem
    
    # Allocate an array to store already computed subproblems
    dp = [None for i in range(n + 1)]
    fib(n, dp) 
    return dp[n] if n > 1 else 1

def climbStairs3(n):
    """
        Using Dynamic Programming; Bottom Up approach in place (with space optimised) Time = O(n), Memory = O(1)
        
        SOLUTION:
        The intuition is to think of climbing stairs like the Fibonacci sequence whereby each step can be reached from either one step before or two steps before
        - We start bottom up. E,g imagine n is 4; i.e we start computing from 4. 
        - Instead of storing all past results, we only keep track of the last two values; i.e ways_one, ways_two
        - We start with 1 way to stay on the ground and 1 way to reach the first step
        - For each step update the number of ways by; 
            - adding the last 2 values (ways_one = ways_one + ways_two)
            - and shifting the previous value( ways_two = temp_ways_one)
        - At the end ways_one holds the answer
         
    """
    ways_one, ways_two = 1, 1 # ways to reach (n-1) and (n-2)
    
    for _ in range(n - 1):
        temp_ways_one = ways_one # Store the current ways_one before updating
        ways_one = ways_one + ways_two # Cureent step is sum of the last 2 steps
        ways_two = temp_ways_one # Update ways_two to the previous ways_one
        
    return ways_one

def climbStairs4(n):
    '''
        Using similar DP approach to fibonacci sequence but starting at 1, 1 instead of 0, 1 as in the case of fibonacci
        Time = O(n), Memory = O(n)
    '''
    if n <= 1:
        return 1
    
    ways_one, ways_two = 1, 1 # ways to reach (n-1) and (n-2)
    
    # Iterate from step 2 up to n
    for _ in range(2, n + 1):
        curr_ways = ways_one + ways_two # Summing the last 2 steps gives the current step
        ways_two = ways_one
        ways_one = curr_ways
        
    return ways_one


if __name__ == '__main__':
    
    for n in range(11):
        print(n, climbStairs4(n))
        assert climbStairs1(n) == climbStairs2(n) == climbStairs3(n) == climbStairs4(n)
    