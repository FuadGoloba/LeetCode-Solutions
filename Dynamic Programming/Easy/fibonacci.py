# Fibonacci Problem 

def fib_brute_force(n):
    '''
        Brute Force Recursive solution to Fibonacci series; Time Complexity - O(2^n) where n is the number to find its fibonacci series
    '''
    if n <= 1:
        return n
    return fib_brute_force(n - 1) + fib_brute_force(n - 2)


def fib_memoization(n, cache):
    '''
        Memoization technique to Fibonacci problem
    '''
    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fib_memoization(n - 1, cache) + fib_memoization(n - 2, cache)
    return cache[n]


def fib_dp(n):
    '''
        Dynamic Programming Technique (Bottom Up Approach)
    '''
    
    if n < 2:
        return n
    
    # create an array to store the 2 numbers to compute the fibonacci of the next number
    dp = [0, 1]
    
    # Compute fibonacci of all numbers up until n by using the previous 2 fibonacci numbers computed
    i = 2
    while i <= n:
        temp = dp[1] 
        dp[1] = dp[0] + dp[1]
        dp[0] = temp
        i += 1
    return dp[1]


def fib_dp2(n):
    '''
        Dynamic Programming Technique (bottom up approach without using an array)
    '''
    
    if n < 2:
        return n
    
    prev, curr = 0, 1
    
    for i in range(2, n + 1):
        temp = curr
        curr = curr + prev # Update current
        prev = temp
    
    return curr
    

if __name__ == '__main__':
    print(fib_brute_force(10))
    print(fib_memoization(10, {}))
    print(fib_dp(10))
    print(fib_dp2(10))