# Implement Stack using Queues

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


# Solution (Logic) - using a queue(FIFO) to implement a stack takes O(1) for all operations except the pop(). 

from collections import deque

class Mystack:
    '''
        Implementing a stack using a queue
    '''
    
    def __init__(self):
        self.queue = deque()
        
    # Push element to the top of the stack or append (works same way a queue does)
    def push(self, x):
        self.queue.append(x)
    
    # pop element from the stack - uses O(n)
    def pop(self):
        # Traverse the queue till until the second to the last element
        for item in range(len(self.queue) - 1):
            self.push(self.queue.popleft()) # pop the left most element from the queue and push back to the top of the stack; At this point, the last element of the queue becomes the top of the stack
        
        return self.queue.popleft() # retuen the top of the stack
    
    # Returns the element on top of the stack without removing it (also called peek)
    def top(self):
        return self.queue[-1]
    
    # Returns True if the stack is empty
    def empty(self):
        return len(self.queue) == 0
    
    def print(self):
        return self.queue
    
    
if __name__ == '__main__':
    
    stack = Mystack()
    for i in range(5):
        stack.push(i)
    
    print(' Pushed 5 elements to the stack')
    print(stack.print())
    print('See the top of the stack')
    print(stack.top())
    print('Pop from the stack')
    print(stack.pop())
    
       
    
    