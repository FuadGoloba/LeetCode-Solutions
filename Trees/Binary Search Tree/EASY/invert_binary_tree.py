# Invert Binary Tree {EASY}

# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
    # Input: root = [4,2,7,1,3,6,9]
''' Construct the following tree
               4
             /    \                                                                     
            /      \
           2         7
          / \       /  \
         /   \     /    \
        1     3   6      9
'''
# Output: [4,7,2,9,6,3,1]
''' Construct the following tree
               4
             /    \                                                                     
            /      \
           7         2
          / \       /  \
         /   \     /    \
        9     6   3      1
'''

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []

class BinarySearchTreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def level_order_traversal(self):
        from collections import deque
        '''
            Using a Breadth First search approach to traverse a BST; 
            - Idea is to traverse on a level order. starting with including the node at each level and then the children of the nodes (left and right) at the next level(2) and the grand children of the previous nodes at the next level(3)
            - It's best solved Iteratively as when we traverse a tree using BFS, we don't go all the way to the depth of every sub tree, rather we go level by level, therefore, we need to store each subtree in order to go back to its children on the next level
        
            Steps:
                - We use a queue (FIFO) to store each node at a level and go through all nodes in a current queue
                - For each node, pop it from the queue and include it values to the result list
                - Then add the node's children (left and right) to the queue for the next level traversal
                - Iteratively repeat the steps above till the queue is empty (i.e we have traversed the entire Tree and its nodes)
        '''
        # result list to store elements traversed
        elements = []
        
        # Create a queue data structure to keep track of each subtree's children nodes as we traverse on each level
        queue = deque()
        
        # Append the first node of the tree to the queue at the first level
        if self:
            queue.append(self)
            
        #level = 0
        # Traverse the tree till we have no node in the queue
        while len(queue) > 0:
            # At each level of the tree, loop over the nodes in the queue, popping them (nodes) and adding their values to the result, then adding their children to the queue for the next level traversal
            for i in range(len(queue)):
                curr = queue.popleft() # we pop the first node that was entered in the queue and add its value into the result list
                elements.append(curr.value)
                
                # Check if the curr node has any children and we add them (nodes) to the stack for the next level traversal
                if curr.left:
                    queue.append(curr.left)
                    
                if curr.right:
                    queue.append(curr.right)
                    
        return elements



# Solution
def invertTree(root):
    
    # return None for an empty Tree
    if not root:
        return None
    
    # Swap the nodes of the left and right subtrees
    root.left, root.right = root.right, root.left
    
    # Recursively invert for children nodes
    invertTree(root.left)
    invertTree(root.right)

    return root


if __name__ == '__main__':
    
    
    ''' Construct the following tree
               4
             /    \                                                                     
            /      \
           2         7
          / \       /  \
         /   \     /    \
        1     3   6      9
    '''
    
    root = BinarySearchTreeNode(4)
    root.left = BinarySearchTreeNode(2)
    root.right = BinarySearchTreeNode(7)
    root.left.left = BinarySearchTreeNode(1)
    root.left.right = BinarySearchTreeNode(3)
    root.right.left = BinarySearchTreeNode(6)
    root.right.right = BinarySearchTreeNode(9)
    
    print("Input:")
    print(root.level_order_traversal())
    
    invertTree(root)
    
    print('Output:')
    print(root.level_order_traversal())
    

