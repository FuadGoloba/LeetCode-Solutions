# Binary Tree Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
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
# Input = [4,0,1,Null,7,3,2,Null,Null,0, Null], targetSum = 7
# Output = true

# Example 3:
''' 
                1
             /    \                                                                     
            /      \
           2        3
'''
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.


class BinaryTreeNode:
    
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
        
    def hasPathSum(self, targetSum, pathSum=0):
        '''
            Using backtracking technique by going through all possible nodes till we find a root-to-leaf path that gives a total value equal to our targetSum. If we stumble on any roadbloack, we backtrack and check another till we find a solution 
            or till we've tried every possible way and can't find a solution, then we return False. (Backtracking uses a Brute-Force approach)
            Time = O(n), Memory = O(height of tree)
        '''
        
        # Case when a root doesn't exist
        if not self:
            return False
        
        # We sum up all values we encounter on a root-to-leaf path
        pathSum += self.val
        
        # Case when we reach a leaf node and check that the sum along that path equals our targetSum
        if not self.right and not self.left:
            if pathSum == targetSum:
                return True

        # Case when we the root node has left subtree, we recursively go through till we get to the leaf node and sum up the values
        if self.left:
            if self.left.hasPathSum(targetSum, pathSum):
                return True
            
        # Case when we the root node has right subtree, we recursively go through till we get to the leaf node and sum up the values
        if self.right:
            if self.right.hasPathSum(targetSum, pathSum):
                return True
        
        # We bacltrack by removing values from our pathSum if the root-to-leaf pathSum doesn't equal our targetSum and check other subtrees if there exists any, else we return False if there exists none
        pathSum -= self.val
            
        return False
        

# To submit on Leetcode
def hasPathSum(root, targetSum):
    
    # Creating a recursive dfs backtracking algotrithm 
    def dfs(TreeNode, pathSum):
        # Case when a root doesn't exist
        if not TreeNode:
            return False
        
        # We sum up all values we encounter on a root-to-leaf path
        pathSum += TreeNode.val
        
        # Case when we reach a leaf node and check that the sum along that path equals our targetSum
        if not TreeNode.right and not TreeNode.left:
            if pathSum == targetSum:
                return True

        # Case when we the root node has left subtree, we recursively go through till we get to the leaf node and sum up the values
        if TreeNode.left:
            if dfs(TreeNode.left, pathSum):
                return True
            
        # Case when we the root node has right subtree, we recursively go through till we get to the leaf node and sum up the values
        if TreeNode.right:
            if dfs(TreeNode.right, pathSum):
                return True
        
        # We bacltrack by removing values from our pathSum if the root-to-leaf pathSum doesn't equal our targetSum and check other subtrees if there exists any, else we return False if there exists none
        pathSum -= TreeNode.val
            
        return False
    
    return dfs(root, 0)

        
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
    root.left.right = BinaryTreeNode(7)
    root.right.left = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(2)
    root.right.left.right = BinaryTreeNode(0)
    
    
    print(root.hasPathSum(7))
    # using Leetcode Solution style
    print(hasPathSum(root, 5))
        
        