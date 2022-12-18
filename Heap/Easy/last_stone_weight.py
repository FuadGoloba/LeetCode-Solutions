# LAST STONE WEIGHT {EASY}

# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
    # If x == y, both stones are destroyed, and
    # If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    # At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

# Example 2:
# Input: stones = [1]
# Output: 1


def lastStoneWeight(stones):
    '''
        Using a Heap data structure to get the heaviest stones
        Time = O(n), memory = O(n)
    '''
    import heapq
    
    # NOte: Since Python's heapq.heappop function only pops the smallest element in a heap, we invert the integers in the array so that popping from the heap will return the largest number
    stones_heap = [-num for num in stones]
    heapq.heapify(stones_heap) # Heapifying the array in order to pop the 2 heaviest stones
    
    # Traverse until we have the last stone
    while len(stones_heap) > 1:
        y = heapq.heappop(stones_heap) # Popping the heaviest stone
        x = heapq.heappop(stones_heap) # Popping the 2nd heaviest stone
        
        if x != y:
            heapq.heappush(stones_heap, y - x)
    
    # Should we have no stones left; we append 0 to return 
    stones.append(0)
    return abs(stones_heap[0])

if __name__ == '__main__':
    for stones in [[2,7,4,1,8,1], [1], [10,49,30,20,5,64,89,35]]:
        print(lastStoneWeight(stones))
        