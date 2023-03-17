# Count Unique Paths - Medium

# Count the number of paths from the top left to the bottom right. You are only allowed to move down or to the right.
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# Example:
# Input: m = 4, n = 4
# Output: 20

# Example 2:
# Input: m = 3, n = 2
# Output: 3

# Example 3:
# Input: m = 3, n = 7
# Output: 28

# Solution: This problem can be solved Recursively (Top Down), using Memoization(Top Down Approach), and also using Dynamic Programming Techniques(Bottom Up approach). This is th eorder from least efiicient to very efficient
#     : The sum of paths from a given cell/coordinate is computed as sum of (count of paths from the cell below it and count of paths from the cell above it)
#     : (e.g count of paths at grid[2][1] = count of paths at grid[3][1] + count of paths at grid[2][2])

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
    
    # Method to compute the sum of paths recursively - Time: O(2 ^ (n + m)), Space: O(n + m)
    def CountUniquePathDFS(self):
        curr_row, curr_col = 0, 0
        # Recursive function to traverse the grid counting all parts when we move down and when we move right
        def DFS(curr_row, curr_col):
            # Base case : 
            if curr_row == self.rows or curr_col == self.cols: # If we are out of bounds
                return 0
            if curr_row == self.rows - 1 and curr_col == self.cols - 1: # We get to the final destination and return 1
                return 1
            
            # Recursively add the count of paths from a cell when we go down and to the right (e.g count of paths at grid[2][1] = count of paths at grid[3][1] + count of paths at grid[2][2])
            return (DFS(curr_row + 1, curr_col) + DFS(curr_row, curr_col + 1))

        return DFS(curr_row, curr_col)
    
    
    # Method to compute the sume of paths using Memoization - Time and Space: O(n * m)
    def CountUniquePathMemoization(self): 
        curr_row, curr_col, cache = 0, 0, dict()
        
        def DFSCache(curr_row, curr_col, cache):
            if curr_row == self.rows or curr_col == self.cols:
                return 0
            
            if (curr_row, curr_col) in cache:
                return cache[(curr_row, curr_col)]
            
            if curr_row == self.rows - 1 and curr_col == self.cols - 1:
                return 1
            
            cache[(curr_row, curr_col)] = DFSCache(curr_row + 1, curr_col, cache) + DFSCache(curr_row, curr_col + 1, cache)
            
            return cache[(curr_row, curr_col)]
        return DFSCache(curr_row, curr_col, cache)
    
    
    # Method to compute sum of paths using Dynamic Programming - Time: O(n * m), Space: O(m), where m is num of cols
    def CountUniquePathDP(self):
        '''
            Unlike the Top Down Approach, we start from the bottom and work our way up. Here we save more space than the memoization method as DP wouldn't need the entire grid to calculate values at a given row
            Since to calculate count of paths for cells in a particular row, we only need its bottom row. e.g grid[rows 2] will need grid[rows 3] and then we update the bottomm row to become the current row
            (i.e grid[rows 2] after being calculated becomes the bottom row to calculate for grid[rows 1])
        '''
        bottom_row = [0] * self.cols # Create an initial bottom most row to be all 0s since they are out of bounds but is needed to calculate the values of the last row of the grid
        
        for row_idx in range(self.rows - 1, -1, -1): # Starting from the last row
            curr_row = [0] * self.cols # create space to compute its values
            curr_row[self.cols - 1] = 1 # The count of path from the last col of any given row will always be 1
            for col_idx in range(self.cols - 2, -1, -1): # Starting from the second to the last column
                curr_row[col_idx] = curr_row[col_idx + 1] + bottom_row[col_idx] # Compute the count of paths from all cells at the current row
            bottom_row = curr_row # update the bottom row to be the current row
            
        return bottom_row[0] # At this point, the bottom row has shifted all the way to the top of the grid and now we can return the total count of paths from the top left corner
            
        

if __name__ == '__main__':
    grid = Grid(3, 7)
    
    print(grid.CountUniquePathDFS())
    print(grid.CountUniquePathMemoization())
    print(grid.CountUniquePathDP())
        