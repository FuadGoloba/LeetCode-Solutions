# Count Unique Paths 2( With Obstacles)

# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# Example 1:
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Example 2:
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1

# Solution: This problem is a similar one to 'Count Unique Path' except that we have to watch out for obstacles that can block a path. 
#     : Similarly, it can be solved Recursively (Top Down), using Memoization(Top Down Approach), and also using Dynamic Programming Techniques(Bottom Up approach). This is th eorder from least efiicient to very efficient
#     : The sum of paths from a given cell/coordinate is computed as sum of (count of paths from the cell below it and count of paths from the cell above it)
#     : (e.g count of paths at grid[2][1] = count of paths at grid[3][1] + count of paths at grid[2][2])

class Grid:
    
    def __init__(self, obstacleGrid):
        self.obstacleGrid = obstacleGrid
        
    # Method to compute the sum of paths recursively - Time: O(2 ^ (n * m)), Space: O(n * m)
    def countUniquePathsWithObstacles(self):
        nrows, ncols = len(self.obstacleGrid), len(self.obstacleGrid[0])
        curr_row_idx, curr_col_idx = 0, 0
        
        def DFS(curr_row_idx, curr_col_idx, nrows, ncols):
            if curr_row_idx == nrows or curr_col_idx == ncols or self.obstacleGrid[curr_row_idx][curr_col_idx] == 1:
                return 0
            if curr_row_idx == nrows - 1 and curr_col_idx == ncols - 1:
                return 1
            return (DFS(curr_row_idx + 1, curr_col_idx, nrows, ncols) + DFS(curr_row_idx, curr_col_idx + 1, nrows, ncols))
        
        return DFS(curr_row_idx, curr_col_idx, nrows, ncols)
    
    # Method to compute the sume of paths using Memoization - Time and Space: O(n * m)
    def countUniquePathsWithObstaclesMemoization(self):
        nrows, ncols = len(self.obstacleGrid), len(self.obstacleGrid[0])
        curr_row_idx, curr_col_idx, cache = 0, 0, {}
        
        def DFSCache(curr_row_idx, curr_col_idx, nrows, ncols, cache):
            if curr_row_idx == nrows or curr_col_idx == ncols or self.obstacleGrid[curr_row_idx][curr_col_idx] == 1:
                return 0
            if (curr_row_idx, curr_col_idx) in cache:
                return cache[(curr_row_idx, curr_col_idx)]
            if curr_row_idx == nrows - 1 and curr_col_idx == ncols - 1:
                return 1
            return (DFSCache(curr_row_idx + 1, curr_col_idx, nrows, ncols, cache) + DFSCache(curr_row_idx, curr_col_idx + 1, nrows, ncols, cache))
        
        return DFSCache(curr_row_idx, curr_col_idx, nrows, ncols, cache)
    
    # Method to compute sum of paths using Dynamic Programming - Time: O(n * m), Space: O(2 * m)== O(m), where m is num of cols
    def countUniquePathsWithObstaclesDP(self):
        '''
            Unlike the Top Down Approach, we start from the bottom and work our way up. Here we save more space than the memoization method as DP wouldn't need the entire grid to calculate values at a given row
            Since to calculate count of paths for cells in a particular row, we only need its bottom row. e.g grid[rows 2] will need grid[rows 3] and then we update the bottomm row to become the current row
            (i.e grid[rows 2] after being calculated becomes the bottom row to calculate for grid[rows 1])
        '''
        nrows, ncols = len(self.obstacleGrid), len(self.obstacleGrid[0])
        bottom_row = [0] * (ncols + 1) # Create the initial bottom row with the inclusion of an additional column for out of bounds cases during computation
        
        for row_idx in range(nrows - 1, -1, -1):
            current_row = [0] * (ncols + 1)
            for col_idx in range(ncols -1, -1, -1):
                if self.obstacleGrid[row_idx][col_idx] == 1: # Check for obstacles
                    current_row[col_idx] = 0
                elif row_idx == nrows - 1 and col_idx == ncols - 1: # Check for the destination coordinate
                    current_row[ncols -1] = 1
                else:
                    current_row[col_idx] = current_row[col_idx + 1] + bottom_row[col_idx]
            bottom_row = current_row
        return bottom_row[0]
                    
    
if __name__ == '__main__':
    grid = Grid([[0,0,0],
                  [0,1,0],
                  [0,0,0]])
    
    grid2 = Grid([[0,1,0,0,0],
                 [1,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0]])
    
    print(grid.countUniquePathsWithObstacles())
    print(grid.countUniquePathsWithObstaclesMemoization())
    print(grid.countUniquePathsWithObstaclesDP())