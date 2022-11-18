# Climbing stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbStairs1(n):
    
    '''
        Using Recursion; Similar solution case to fibonacci sequence since a person can reach nth step from either (n-1)th step or from (n-2)th step
        Except that the number of ways to climb to the top is fib(n + 1)
        Time = O(2n), 
    '''
    def fib(n):
        if n <= 1:
            return 1
        
        return fib(n-1) + fib(n - 2)
    
    # returns the count of ways to climb to the top
    return fib(n + 1)

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
    one, two = 1, 1
    
    for i in range(n - 1):
        
        temp = one # temporary variable to store the value of one before updating it
        one = one + two # Update one
        two = temp # update two to be temp which is the previous value of one
        
    return one


def climbStairs4(n):
    '''
        Using similar SP approach to fibonacci sequence but starting at 1, 1 instead of 0, 1 as in the case of fibonacci
    '''
    if n <= 1:
        return n
    
    n1, n2 = 1, 1
    
    for i in range(2, n + 1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
        
    return n2


if __name__ == '__main__':
    
    for n in range(8):
        print(n, climbStairs3(n))
    