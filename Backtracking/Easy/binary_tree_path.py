# Binary Tree Path

# Given a Binary Tree, Write two functions to; 
    # Determine if a path exists from the root of the tree to a leaf node Returns True otherwise False. It may not contain a node with zero
    # Return the path that exists if it is guaranteed that at most one path could exist.
    
    
# Example

''' 
               4
             /    \                                                                     
            /      \
           0        1
            \      /  \
             \    /    \
              7  3      2
                 \             
                  \
                   0   
'''

# Output:
    # 1. True
    # 2. [4,1,2]
    

class BinaryTreeNode:
    
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
    # Method to determine if a path exists without any nodal zeros
    def canReachLeaf(self):
        '''
            Using backtracking technique by going through all possible nodes till we find a path that exists. If we stumble on any roadbloack, we backtrack and check another till we find a solution 
            or till we've tried every possible way and can't find a solution, then we return False. (Backtracking uses a Brute-Force approach)
        '''
        
        # Case when root does not exist or we're at a node that contains 0
        if not self or self.val == 0:
            return False
        
        # Case when we finally reach a leaf node
        if not self.left and not self.right:
            return True
        
        # Case when root node has a left subtree; we recursively check if path exists and backtrack to its root if True or False
        if self.left:
            if self.left.canReachLeaf():
                return True
        
        # Case when root node has a right subtree; we recursively check if path exists and backtrack to its root if True or False
        if self.right:
            if self.right.canReachLeaf():
                return True
        
        # Return False if no path exists
        return False
    
    
    # Method to print a path and return true if a path exists
    def leafpath(self, path = []):
        
        # Case when root does not exist or we're at a node that contains 0
        if not self or self.val == 0:
            return False
        
        # Add the root if it satisifies the condition
        path.append(self.val)
        
        # Case when we finally reach a leaf node
        if not self.right and not self.left:
            print(path)
            return True
        
        # Case when root node has a left subtree; we recursively check if path exists and backtrack to its root if True or False
        if self.left:
            if self.left.leafpath(path):
                return True
        
        # Case when root node has a right subtree; we recursively check if path exists and backtrack to its root if True or False
        if self.right:
            if self.right.leafpath(path):
                return True
        
        # We pop the cyrrent node from the path if it fails the condition; (contains zero or doesn't lead us to a leaf node) and then we backtrack
        path.pop()
        
        return False
    
    
    
if __name__ == '__main__':
    
    ''' 
               4
             /    \                                                                     
            /      \
           0        1
            \      /  \
             \    /    \
              7  3      2
                 \             
                  \
                   0   
'''

    root = BinaryTreeNode(4)
    root.left = BinaryTreeNode(0)
    root.right = BinaryTreeNode(1)
    root.right.left = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(2)
    root.right.left.right = BinaryTreeNode(0)
    
    print('Does a path exist:')
    print(root.canReachLeaf())
    print(root.leafpath())
