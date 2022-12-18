# Heap / Priority Queue Data Structure

# Heap data structure is mainly used to represent a priority queue for retrieving (minimum/maximum) values
# A heap can be a Tree-based data structure whereby the tree is a complete binary tree (and not a binary search tree).
# Its benefits over a binary search tree is that, it allows returning or searching priority elements (minimum / maximum) elements in O(1) time
# Implementing a Heap data structure (Tree-based) must satisfy 2 properties
            # 1. Structure Property - Must be a complete binary tree in which nodes are entered in a level order traversal from left to right such that only rightmost of the last level can be leaf nodes 
            # 2. Order Property - Based on the order, there can be a minHeap or a maxHeap.
                # MinHeap order must be satisfied such that any parent must be the smallest of its tree and is recursively so for its children
                # Max Heap order must be satisfied such that any parent must be the largest of its tree and is recursively so for its children

# The heap data structrure can be implemented in an array/list format                                                             
# Example: LEt's look at a minimum Heap below that satisfies both order and structure property.
''' 
               14
             /    \                                                                     
            /      \
           16       19
          /  \      /  \
         /    \    /    \
        21    17  19     68
       /  \                     
      /    \       
    65     30
'''                                                            
# Implementing the min Heap in an array/list format would have their values at the following indices (Note; we start the 0th index with None or any value)
    # left child at index = 2 * curr index
    # right child at index = (2 * curr index) + 1 
    # Parent at index = curr index // 2
    
    # Therefore the above tree structure can be added in the Heap data structure resulting in [x, 14, 16, 19, 21, 17, 19, 68, 65, 30]

class Heap:
    '''
        parent = index // 2
        left child = 2 * index
        right child = (2 * index) + 1
        
        Note: This implementation is assuming a Minimum Heap
    '''
    
    def __init__(self):
        self.heap = [0] # The 0th index of the Heap is a placeholder 
        
    
    # Method to push a value to the Heap O(logn)
    def push(self, val):
        
        # First append the value to the Heap (Satisfying the Structure property)
        self.heap.append(val)
        
        idx = len(self.heap) - 1 # Get the index of the new value in the heap to track if it's order property is right
        
        # RE-ARRANGING THE HEAP
        # Iteratively swap the new value till it satisfies the order property of the heap (i.e check that at it's current position, (if it's a minHeap) its parent is not greater than the new value)
        # Note - parent is at a position (index of value // 2)
        while idx > 1 and self.heap[idx // 2] > self.heap[idx]:
            self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx] # Swap the position of the current parent and the new value
            idx //= 2 # Update to the position of the 'grandparent' (if it exists) and check if it satisfies the order property
            

    # Method to pop priority element (i.e minimum element in this case) O(logn)
    def pop(self):
        '''
            Idea is to pop priority element while maintaining its Order property and Structure property.
            i. To satisfy Structure Property:
                Pop the priority element from the Heap by replacing its node with the last node in the Heap.
                Note: This helps maintain the structure property but breaks the order property as the last element would now be the first element in the Heap and would be larger than its children nodes.
                
            ii. To satisfy the Order Property:
                For the first element (node), get the minimum of its children and swap with it. 
                Check that its new children satisfies the order property or repeat by swapping with its minimum
        '''
        
        # case when there's no value in the Heap
        if len(self.heap) == 1:
            return 
        
        # case when there's one value in the heap, we pop the elment
        if len(self.heap) == 2:
            return self.heap.pop()
        
        
        # ---------- case when we have more than 1 --------------------------- #
        # case when we have 2 values
        res = self.heap[1] # We first create a copy of the value and store in a variable to return at the end 
        
        self.heap[1] = self.heap.pop() # We move the last value in the heap to the root/head e.g [X, 14, 16] to remove 14 becomes [X, 16]
        
        # Case when we have more than 2 values (We need to be careful in order to maintain the order and structure property)
        idx = 1 # starting at the first actual element of the heap (root)
        
        # Percolate down
        while 2 * idx < len(self.heap):
            # case 1: Re-ordering when a parent/root has left and right children and the order property is not satisfied
            if (2 * idx + 1 < len(self.heap) # if right child exists
                and self.heap[2 * idx + 1] < self.heap[2 * idx] # and value at right child is greater than the value at the left child
                and self.heap[idx] > self.heap[2 * idx + 1]): # and value at parent is higher than the value at right child,
                    # Swap the right child with the parent and point to the position of the right child
                    self.heap[2 * idx + 1], self.heap[idx] = self.heap[idx], self.heap[2 * idx + 1]
                    idx = 2 * idx + 1 
            
            # case 2 : Reo-rdering when a parent has only a left child and the order property isnt satisfied (i.e parent > left child)
            elif self.heap[idx] > self.heap[2 * idx]:
                # swap the left child with the Parent and move our pointer to the position of the left child
                self.heap[idx], self.heap[2 * idx] = self.heap[2 * idx], self.heap[idx]
                idx = 2 * idx
                
            # case 3: We break as we are already satisfying the order property
            else:
                break   
            
        # Now we return the priority element
        return res 
                
                
    # Method to heapify an array/list
    def heapify(self, arr):
        # Satisfying the Structure property by creating a heap with a zeroth index
        self.heap += arr
        
        # Satisfying the Order proerty by comparing parent nodes with their children
            # Skipping nodes without children; so we start at parent nodes
        curr_idx = (len(self.heap) - 1) // 2 # gives us the last parent node and we work our way up till the start of the Heap
        
        while curr_idx > 0:
            # Percolate down
            idx = curr_idx
            
            while 2 * idx < len(self.heap):
                # case 1: Re-ordering when a parent/root has left and right children and the order property is not satisfied
                if (2 * idx + 1 < len(self.heap) # if right child exists
                    and self.heap[2 * idx + 1] < self.heap[2 * idx] # and value at right child is greater than the value at the left child
                    and self.heap[idx] > self.heap[2 * idx + 1]): # and value at parent is higher than the value at right child,
                        # Swap the right child with the parent and point to the position of the right child
                        self.heap[2 * idx + 1], self.heap[idx] = self.heap[idx], self.heap[2 * idx + 1]
                        idx = 2 * idx + 1 
                
                # case 2 : Reo-rdering when a parent has only a left child and the order property isnt satisfied (i.e parent > left child)
                elif self.heap[idx] > self.heap[2 * idx]:
                    # swap the left child with the Parent and move our pointer to the position of the left child
                    self.heap[idx], self.heap[2 * idx] = self.heap[2 * idx], self.heap[idx]
                    idx = 2 * idx
                    
                # case 3: We break as we are already satisfying the order property
                else:
                    break
            # Move to the prev idx
            curr_idx -= 1
            
            
            
if __name__ == '__main__':
    
    #------- Heapifying an array ------#
    hp = Heap()
    hp.heapify([60,50,80,40,30,10,70,20,90])
    print(hp.heap[1:])
    
    
    # ----------------Pushing values into a heap ----------------#
    hp2 = Heap()
    for val in [17, 14, 19, 21, 68, 26, 30, 65, 19, 16]:
        hp2.push(val)
    print(hp2.heap[1:])
    # Popping a priority element from a heap (minimum element)
    hp2.pop()
    print(hp2.heap[1:])