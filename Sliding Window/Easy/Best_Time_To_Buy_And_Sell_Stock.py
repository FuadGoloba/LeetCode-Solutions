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
        Return the maximum profit you can achieve from this transaction. Using Sliding WWindow approach

        INTUITION:
            The intuition is to use a greedy sliding window approach with 2 pointers; buy_price and sell_price, representing when a stock is bought and when it is sold respectively. 
            The idea to maximise profit is to find the day with the lowest price to buy stock (i.e lowest buy_price). This value will only be updated when we find a day with stock price lower than it;s current value.
            We will keep traversing with sell_price through all of the prices in the future to sell while calculating the profit for each of these days and storing the max at each iteration. 
            Should we find a price at sell_price (future) lower than the current day we bought (buy_price), we update buy_price=sell_price to be the new lowest stock price day and try to find a future sell_price with a profit higher than what was found previously.

        Steps:
            1. set 2 pointers; buy_price and sell_price to 0 and 1 respectively and max_profit to 0
            2. while sell_price is less than the length of prices, we do the following
                a. if the price at buy_price is less than the price at sell_price, compute the profit and update max_profit
                b. if the price at sell_price is less than the price at buy_price, update buy_price to be the new day we bought stock
                c. move sell_price to the next day
            3. return max_profit found at the end of the traversal 

        Time Complexity: O(n) since we are traversing through the list of prices once with sell_price pointer
        Space Complexity: O(1) since we are using a constant amount of space to store buy_price, sell_price and max_profit
    '''
    buy_price, sell_price, max_profit = 0, 1, 0

    while sell_price < len(prices):
        if prices[buy_price] < prices[sell_price]: # if the current day we bought is less than the current day we are selling, we calculate profit and update max_profit if it is higher than the current max_profit
            profit = prices[sell_price] - prices[buy_price]
            max_profit = max(profit, max_profit)
        else:
            buy_price = sell_price # if the current day we bought is higher than the current day we are selling, we update buy_price to be the new day we bought stock
        sell_price += 1
    return max_profit

def maxProfit3(prices):
    '''
        Return the maximum profit you can achieve from this transaction. Using Dynamic Programming approach

        INTUITION:
            The intuition is to use a greedy approach to keep track of the minimum price we have seen so far (min_price) and the maximum profit we can achieve at each iteration (max_profit). 
            We will traverse through the list of prices and at each iteration, we will update min_price if we find a price lower than it and calculate the profit for the current price by subtracting min_price from it. We will then update max_profit if the calculated profit is higher than the current max_profit. 
            This way, we are always keeping track of the lowest price we have seen so far and the maximum profit we can achieve at each iteration.
            
        Steps:
            1. Initialise min_price to the first price in the list
            2. Initialise max_profit to 0
            3. Traverse through the sell prices
                a. Update min_price if we find a price lower than it
                b. Calculate profit for the current price by subtracting min_price from it and update max_profit if the calculated profit is higher than the current max_profit
            4. Return max_profit found at the end of the traversal
            
        Time Complexity: O(n) since we are traversing through the list of prices once
        Space Complexity: O(1) since we are using a constant amount of space to store min_price and max_profit  
    '''
    
    min_price = prices[0] # initialise min_price to the first price in the list
    max_profit = 0
    
    for sell in prices:
        min_price = min(min_price, sell) # update min_price if we find a price lower than it
        max_profit = max(max_profit, sell - min_price) # calculate profit for the current price and update max_profit if it is higher than the current max_profit

    return max_profit
    

if __name__ == '__main__':
    for input_n in [[7,1,5,3,6,4], [7,6,4,3,1], [7,1,5,3,6,4,10]]:
        print(maxProfit2(input_n))
        assert maxProfit2(input_n) == maxProfit3(input_n)
    