# Binary Search Tree is a type of Binary tree (every node can only have a maximum of 2 child nodes) that has a sorted property whereby 

# - The left subtree of a node contains only nodes with keys lesser than the node's key
# - The right subtree of a node contains only nodes with keys greater than the node's keys
# - The left and right subtree each must also be a binary search tree
# - There must be no duplicate nodes (BST can be used to implement a set data structure)

# * Searching for a value in the binary search tree takes O(logn) operations
# * insering an element in the BST takes O(logn)

# Note: The benfit of a binary search tree over binary search on a sorted array is that; inserting or removing from a BST is more efficient than from a sorted array:
    # search in a sorted array using binary search takes O(logn); same as search in a BSt takes O(logn)
    # Insertion or deletion from an array takes O(n) while in a BST, O(logn) which is the major benefit of having the BST value structure
    
# Note: A BST can be used to implement a SET data structure as BST allows no duplicate values

class BinarySearchTreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    #Adding value or insert to the tree    
    def add_child(self, value):
        # check to see if the value already exists
        if value == self.value:
            return 
        
        # Adding to the left side of the tree
        if value < self.value:
            # check that the left side of that tree node is not empty and recursively check till we get to a leaf node
            if self.left:
                self.left.add_child(value) # add the value recursively 
            else: # The left side of the tree node is empty and we can easily add the element. Note that the element is also an object of BinarySearch TreeNode
                self.left = BinarySearchTreeNode(value)
                
        else: # Adding value to the right side of the tree
            if self.right: # Check that the right side of the tree node is not empty and recursively check till we get to a leaf node
                self.right.add_child(value)
            else:
                self.right = BinarySearchTreeNode(value)
                 
                
    # Method to find minimum value in the tree (Since all ninum values can be found on the left side of the BST)
    def find_min(self):
        if not self.left: # If we are at a leaf node on the left, we are at the minimum of that BST
            return self.value # so we return the value
        return self.left.find_min() # and recursively find the minimum value (i.e the leaf node on the left sub tree)
    
    # Method to find maximum value in the tree (Since all maximum values can be found on the right side of the BST)
    def find_max(self):
        if  not self.right: # If we are at a leaf node on the right, we are at the maximum of that BST
            return self.value
        return self.right.find_max()
        
    
    def delete(self, val):
        # Recursively search the left subtree till we get to the node whose value to be deleted
        if val < self.value: # Check that the vakue to be deleted is on the left side of the tree
            if self.left: # Check that the left sub tree is not empty or NOne
                self.left = self.left.delete(val) # Recursively delete and assign a new subtree to the left node
        
        # Recursively search the left subtree till we get to the node whose value to be deleted
        elif val > self.value:
            if self.right:
                self.right = self.right.delete(val)     
        
        # Case when we find the node to be deleted
        else:
            # if the node to be deleted has no children, then we easily delete it (Deleting a node with no child)
            if self.left is None and self.right is None: #
                return None
            
            # Deleting a node with one child on the right
            if self.left is None: # Check that there exists a right node and not a left, and return that node that exists back to the root node so the current node gets deleted
                return self.right
            
            # Deleting a node with one child on the left
            if self.right is None: # Check that there exists a right node and not a left, and return that node that exists back to the root node so the current node gets deleted
                return self.left
            
            # Deleting a node with children (both left and right nodes) by replacing the value to be deleted with the minimum value on the right subtree
            min_val = self.right.find_min() # We get the minimum value of of the right sub tree to replace the value to be deleted
            self.value = min_val # We copy that minimum value to the current node 
            self.right = self.right.delete(min_val) # Delete the duplicate node (which is the min value that was created)
            
        return self
    
    
    # Method to search for a value in a tree
    def search(self, val):
        # Check the base case; the value is in the root node. Note that every subtree has a root node (recursively)
        if val == self.value:
            return True

        # Recursively search the left side of the tree if the val exists there
        if val < self.value:
            if self.left: # if the left sub tree is not empty, recursively search all nodes on the left 
                return self.left.search(val)
            else: # We've searched all nodes and can't find the elemnent
                return False
         
        # Recursively search the right side of the tree if the val exists   
        else:
            if self.right:  # if the right sub tree is not empty, recursively search all nodes on the right
                return self.right.search(val)
            else:
                return False
    
    # DFS
    # Method to traverse the tree using in-order traversal - In order traversal returns an output with the tree sorted in ascending order
    def in_order_traversal(self):
        '''
            Visit the left subtree first, then visit the root node, and then visit the right subtree ( O(n))
        '''
        elements = [] # array to store the sorted elements
        
        # Visit the left subtree 
        if self.left:
            elements += self.left.in_order_traversal() # Recursively visit the left subtree till we get to a leaf node
        
        # Add the root of each traversal
        elements.append(self.value)
        
        # Visit the right subtree
        if self.right:
            elements += self.right.in_order_traversal() # Recursiely visit the right subtree till we get to a leaf node
        
        return elements
    
    # Pre-order traversal
    def pre_order_traversal(self):
        '''
            Visit the root first, then theh left subtree and then visit the right subtree ( O(n))
        '''
        elements = [] # array to store elements
        
        # Add the root of each traversal first
        elements.append(self.value)
        
        # Visit the left subtree
        if self.left:
            elements += self.left.pre_order_traversal() # Recursively visit the left subtree and add its root
        
        # Visit the right subtree
        if self.right:
            elements += self.right.pre_order_traversal() # Recursively visit the right subtree and add its root
            
        return elements
    
    # Post-order TRaversal
    def post_order_traversal(self):
        '''
            Visit the left subtree first, then the right subtree, then the root node ( O(n)) 
        '''
        elements = []
        
        # Visit the left subtree
        if self.left:
            elements += self.left.post_order_traversal() # Recursively visit the left subtree until we get to its leaf node
        
        # Visit the right subtree
        if self.right:
            elements += self.right.post_order_traversal() # Recursively visit the right subtree until we get to its leaf node
        
        # Add the root of each traveral last
        elements.append(self.value) 
        
        return elements
    
    
    # BFS
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
                    
                
        
# Helper function to build a tree with an array of elements
def build_tree(elements):
    '''Takes a list of elements to build a tree with'''
    root = BinarySearchTreeNode(elements[0]) # Create root node with the first element in the list
    
    # Traverse the list one element after the other and add that element to the tree
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root


if __name__ == '__main__':
    #--------------------------------------- Building a BST from list of elments ------------#
    numbers = [17, 40, 20, 9, 18, 3, 15, 6]
    numbers_tree = build_tree(numbers)
    
    print(numbers_tree.search(15))
    print(numbers_tree.search(60))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    numbers_tree.delete(15)
    print(numbers_tree.in_order_traversal())
    
    
    #--------------------------------------  DFS Traversal -----------------------------------#
    
    ''' Construct the following tree
               15
             /    \                                                                     
            /      \
           12       27
          / \       /  \
         /   \     /    \
        7     14   20   88
                  / \
                 /   \
                      23
    '''
 
    root = BinarySearchTreeNode(15)
    root.left = BinarySearchTreeNode(12)
    root.right = BinarySearchTreeNode(27)
    root.left.left = BinarySearchTreeNode(7)
    root.left.right = BinarySearchTreeNode(14)
    root.right.left = BinarySearchTreeNode(20)
    root.right.right = BinarySearchTreeNode(88)
    root.right.left.right = BinarySearchTreeNode(23)
    
    print(root.in_order_traversal())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())
    
    
# ------------------------------------------- BFS Traversal ----------------------------------------------#

    ''' Construct the following tree and traverse using BFS
    
               4
             /    \                                                                     
            /      \
           3        6
          /        /  \
         /        /    \
        2         5     7

    '''
    
    root = BinarySearchTreeNode(4)
    root.left = BinarySearchTreeNode(3)
    root.right = BinarySearchTreeNode(6)
    root.left.left = BinarySearchTreeNode(2)
    root.right.left = BinarySearchTreeNode(5)
    root.right.right = BinarySearchTreeNode(7)
    
    print(root.level_order_traversal())
    
    
    