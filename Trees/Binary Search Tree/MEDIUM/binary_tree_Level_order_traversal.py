# Binary Tree Level Order Traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1;


# Input: root = [3,9,20,null,null,15,7]

''' 
    
               3
             /    \                                                                     
            /      \
           9        20
                   /  \
                  /    \
                15      7
        
    '''


# Output: [[3],[9,20],[15,7]]


# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []


class BinarySearchTreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
# BFS or Level Order Traversal of a BST
def levelOrder(root):
    from collections import deque
    
    result = []
    # Create a queue data structure to keep track of each subtree's children nodes as we traverse on each level
    queue = deque()
        
        # Append the first node of the tree to the queue at the first level
    if root:
        queue.append(root)
    
    # Traverse the tree till we have no node in the queue    
    while queue:
        # At every level of the tree we initialise an array to store the node values at that level
        level_arr = []
        for i in range(len(queue)):
            curr = queue.popleft() # we pop the first node that was entered in the queue and add its value into the result list
            level_arr.append(curr.value) # add the node's values to the level array
            
            # Check if the curr node has any children and we add them (nodes) to the stack for the next level traversal
            if curr.left:
                queue.append(curr.left)
                
            if curr.right:
                queue.append(curr.right)
                
        # We append the level_arr at each level to the result list   
        result.append(level_arr)
        
    return result


if __name__ == '__main__':
    
    ''' 
               3
             /    \                                                                     
            /      \
           9        20
                   /  \
                  /    \
                15      7
        
    '''
    
    root = BinarySearchTreeNode(3)
    root.left = BinarySearchTreeNode(9)
    root.right = BinarySearchTreeNode(20)
    root.right.left = BinarySearchTreeNode(15)
    root.right.right = BinarySearchTreeNode(7)

    print(levelOrder(root))