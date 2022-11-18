# MinStack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


class MinStack:
    '''
        Implementing a Stack to perform operations in O(1) time
    '''
    
    def __init__(self):
        # Initialise 2 stack attributes; one to store the value and the other to store the minimum value present in the stack; 
        self.stack = []
        self.min_stack = []
        
    def push(self, val):
        # Operation to push a value to the stack
        self.stack.append(val)
        
        # At every push/entry of a new value, we compute the minimum value of the stack at that entry
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)
        
    def pop(self):
        # Operation to pop from the stack; We pop from both stack so we can also have the minimum value of the stack at the current state of the pop
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        # Operation to get the top of the stack
        return self.stack[-1]
    
    def getMin(self):
        # Operation to retuen minimum value in the stack in O(1)
            # With the help of the helper 'min_stack' used to track and store the minimum value at each entry/push of a value, we can return the min value from the min_stack
        return self.min_stack[-1]
        
        