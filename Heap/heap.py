# Heap / Priority Queue Data Structure



class Heap:
    '''
        parent = index // 2
        left child = 2 * index
        right child = (2 * index) + 1
        
        Note: The implementation is assuming a Minimum Heap
    '''
    
    def __init__(self):
        self.heap = [0] # The 0th index of the Heap is a placeholder 
        
    
    # Method to push a value to the Heap O(logn)
    def push(self, val):
        
        # First append the value to the Heap 
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
                
                    

if __name__ == '__main__':
    hp = Heap()
    for val in [17, 14, 19, 21, 68, 26, 30, 65, 19, 16]:
        hp.push(val)
        
    print(hp.heap[1:])
    
    hp.pop()
    
    print(hp.heap[1:])