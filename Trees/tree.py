# A tree Data structure is non-linear and stores hierarchical data. A Tree would have 
# - a root node - which has no parent
# - Parent node - 
# - a child - has child nodes and a parent node
# - a leaf node - has no chuld nodes 

# This data structure is a specialized method to organize and store data in the computer to be used more effectively. 
# It consists of a central node, structural nodes, and sub-nodes, which are connected via edges. We can also say that tree data structure has roots, branches, and leaves connected with one another. 

class TreeNode:
    
    def __init__(self, value):
        self.children = [] # A tree object would have children and every child is also a tree object that would have its own children as well
        self.value = value # A tree object would have a value
        self.parent = None # A tree object could have a parent if its not the root Node
        
    # Method to append a child to a tree
    def add_child(self, child):
        ''' child is also a tree object '''
        child.parent = self # Since child is also a tree object then we can say that the parent of that child is self (i.e we assign the Tree as a parent to the Child)
        self.children.append(child) # adding a child to the list of children
        
    # Method to get number of levels or edges     
    def get_level(self):
        level = 0 
        p = self.parent # 
        # Traverse the parent node one after the other 
        while p:
            level += 1
            p = p.parent # update the parent to the next parent
        return level # return the level count
    
    # Method to print tree 
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|--' if self.parent else ''
        print(prefix + self.value) # Print the root
        # Iterate through the children and recuresively print the children of each child
        for child in self.children:
            child.print_tree()


# Build a product tree
def build_product_tree():
    # Create a root
    root = TreeNode('Electronics')
    
    # Create a child(Laptop) of the root which is also a parent to other children below
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))
    
    # Create a child(television) of the root which is also a parent to other children below
    television = TreeNode('Television')
    television.add_child(TreeNode('Samsung'))
    television.add_child(TreeNode('Sharp'))
    television.add_child(TreeNode('LG'))
    
    # Create a child(mobilephone) of the root which is also a parent to other children below
    mobilephone = TreeNode('Mobile Phone')
    mobilephone.add_child(TreeNode('iPhone'))
    mobilephone.add_child(TreeNode('Google Pixel'))
    mobilephone.add_child(TreeNode('Techno'))
    
    # Add all the children and descendants to the root
    root.add_child(laptop)
    root.add_child(television)
    root.add_child(mobilephone)
    
    return root
    
if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()