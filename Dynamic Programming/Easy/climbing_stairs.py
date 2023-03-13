# Climbing Stairs

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

def climbStairs_BruteForce(n):
    '''
        Using Fibonacci series to solve - Time Complexity - O(2^n) where n is the number to find its fibonacci series
    '''
    def fib(n):
        if n <= 1:
            return n
        
        return fib(n - 1) + fib(n - 2)
    
    # FIbonacci of n + 1 gives the number of ways to reach the n top
    return fib(n + 1)


def climbStairs_memoization(n):
    cache = {}
    def fib(n):
        if n <= 1:
            return n
        
        if n in cache:
            return cache[n]
        
        cache[n] = fib(n - 1) + fib(n - 2)
        
        return cache[n]
    
    return fib(n + 1)


def climbStairs_dp(n):
    if n <= 1:
        return n

    n1, n2 = 1, 1

    for i in range(2, n + 1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2    

if __name__ == '__main__':
    
    print(climbStairs_BruteForce(10))
    print(climbStairs_memoization(10))    
    print(climbStairs_dp(10))
    
    