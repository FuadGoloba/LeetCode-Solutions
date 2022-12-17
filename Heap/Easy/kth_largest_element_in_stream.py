# Kth Largest Element in a Stream

# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


# Example:

# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]

# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8

# Note
# Heap data structure is mainly used to represent a priority queue. In Python, it is available using the “heapq” module. 
# The property of this data structure in Python is that each time the smallest heap element is popped(min-heap). 
# Whenever elements are pushed or popped, heap structure is maintained. The heap[0] element also returns the smallest element each time.

# NAIVE SOLUTION
# A naive solution to the problem would be to use a dynamic array (list), sort the array and get kth largest element. And for the add operation,
# inserting into an array takes O(n) operation.

# EFFICIENT SOLUTION
# An efficient solution is to use a heap data stuctureas it allows us to represent a priority queue (can get min/max values in O(1) time).
# Also, inserting/push and pop operations in a heap data structure takes O(logn) time which makes it more efficient than using an array in ths context.
# The idea of the solution:
    # Since we are concerned with the Kth largest element, we will have to create a minHeap of size K elements. 
    # So that means the minimum element of the heap is our Kth largest element.
        # E.g Kthlargest(3, [4,5,8,2]); we create a minHeap by popping the minimum elements till we get a size of 3; [4,5,8]
        # Now we see that the minimum element at the minHeap of size K is our Kth largest element; which is 4
    # When we add new values to the stream, we will make sure to pop the minimum element after we add this new value until we arrive at minHeap of size K
    # and then we can return the Kth largest element 
    
    
import heapq

class KthLargest:
    
    def __init__(self, k, nums):
        self.minHeap = nums
        self.k = k
        
        # Creating a minHeap of size K elements
        heapq.heapify(self.minHeap) # We convert the array to a heap - O(n)
        # Popping from the heap till it's of size K elements
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
    
    # Method to push a value to the stream 
    def add(self, val):
        # Adding a new value to the stream
        heapq.heappush(self.minHeap, val)
        
        # After adding the new value we want to maintain the size of the minHeap to be of K
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # Return the minimum element of the minHeap which is also the Kth largest element in the stream    
        return self.minHeap[0]
    
    
if __name__ == '__main__':
    
    stream = KthLargest(3, [4,5,8,2])
    
    for val in [3, 5, 10, 9, 4]:
        print(f'Adding {val} to stream gives {stream.add(val)} as the 3rd largest value in the stream')
        
            
        
        
        
