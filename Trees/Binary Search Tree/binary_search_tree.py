# Binary Search Tree is a type of Binary tree (every node can only have a maximum of 2 child nodes) that has a sorted property whereby 

# - The left subtree of a node contains only nodes with keys lesser than the node's key
# - The right subtree of a node contains only nodes with keys greater than the node's keys
# - The left and right subtree each must also be a binary search tree
# - There must be no duplicate nodes

# * Searching for a value in the binary search tree takes O(logn) operations
# * insering an element in the BST takes O(logn)

# Note: The benfit of a binary search tree over binary search on a sorted array is that; inserting or removing from a BST is more efficient than from a sorted array:
    # search in a sorted array using binary search takes O(logn); same as search in a BSt takes O(logn)
    # Insertion or deltion from an array takes O(n) while in a BST, O(logn) which is the major benefit of having the BST value structure

class BinarySearchTreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    # Adding value to the tree    
    def add_child(self, value):
        # check to see if the value already exists
        if value == self.value:
            return 
        
        # Adding to the left side of the tree
        if value < self.value:
            # check that the left side of that tree node is not empty and recursively check till we get to a leaf node
            if self.left:
                self.left.add_child(value)
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
        
        
# Helper function to build a tree
def build_tree(elements):
    '''Takes a list of elements to build a tree with'''
    root = BinarySearchTreeNode(elements[0]) # Create root node with the first element in the list
    
    # Traverse the list one element after the other and add that element to the tree
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root


if __name__ == '__main__':
    numbers = [17, 40, 20, 9, 18, 3, 15, 6]
    numbers_tree = build_tree(numbers)
    
    print(numbers_tree.search(15))
    print(numbers_tree.search(60))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    