"""Best Time to Buy and Sell Stock {EASY}
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
"""

def maxProfit(prices):  
    '''
        Using Brute Force; Time= O(n2)
    '''
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            current = -prices[i] + prices[j]
            max_profit = max(current, max_profit)
    return max_profit

def maxProfit2(prices):
    '''
        Using Sliding Window approach = Time - O(n), Memory - O(1)
        
        SOLUTION:
            The intuition is to use a greedy sliding window approach with 2 pointers; l and r, representing when a stock is bought and when it is sold respectively. 
            The idea to maximise profit is to find the day with the lowest price to buy stock (i.e lowest l). This value will only be updated when we find a day with stock price lower than it;s current value.
            We will keep traversing with r through all of the prices in the future to sell while calculating the profit for each of these days and storing the max at each iteration. 
            Should we find a price at r (future) lower than the current day we bought (l), we update l=r to be the new lowest stock price day and try to find a future r with a profit higher than what was found previously.
    '''
    max_profit = 0
    left_ptr = 0
    right_ptr = 1
    
    # Traverse the prices array
    while right_ptr < len(prices):
        profit = prices[right_ptr] - prices[left_ptr]
        max_profit = max(profit, max_profit)
        # Check if a lower stock price to buy has been found
        if prices[right_ptr] < prices[left_ptr]:
            left_ptr = right_ptr
        right_ptr += 1
        
    return max_profit

if __name__ == '__main__':
    for input_n in [[7,1,5,3,6,4], [7,6,4,3,1], [7,1,5,3,6,4,10]]:
        print(maxProfit2(input_n))
    
    