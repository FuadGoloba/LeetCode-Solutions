# Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Solution - This is a pproblem that can be solved using the idea of a Graph (Adjacent Matrix). 
#          - The grid can be traversed using DFS or BFS 

import collections

def numIslands(grid):
    """
        Using a breadth first search traversal algorithm; Time - O(m * n); Space: O(m * n)
    """    
    # Get the length of the rows and columns in the matrix
    row_len, col_len = len(grid), len(grid[0])
    visited = set() # Set to keep track of visited coordinates
    num_of_islands = 0 # Counter for number of islands
    
    # Creating a dfs algorithm to traverse lands to find an island
    def dfs_isIsland(row_ptr, col_ptr):
        # Base Case
        # Setting conditions to spot traversals that aren't connected to an island
            # Check if the row ptr is out of bound of the matrix's row axes
            # Check if the col_ptr is out of bound of the matrix's col axes
            # Check if the coordinate is not a land
            # Check if it's a land that has been visited before
        if (row_ptr not in range(row_len)
            or col_ptr not in range(col_len)
            or grid[row_ptr][col_ptr] == '0'
            or (row_ptr, col_ptr) in visited
        ):
            return 
        
        # Updated to include the current coordinate (land) we're at
        visited.add((row_ptr, col_ptr))
        
        # Initialise the adjacent coordinates based on the direction of traversal and 
        # Traverse every visited land's neighbour to check if they are part of the connected island;
        directions = [[0,-1], [1,0], [0,-1], [0,1]]
        for r, c in directions:
            adj_row_ptr = row_ptr + r 
            adj_col_ptr = col_ptr + c
            dfs_isIsland(adj_row_ptr, adj_col_ptr)
            
    # Traversing the entire grid to find connected islands
    # Note: AN island is a connection of adjacents lands horizontally or vertically
    for row_ptr in range(row_len):
        for col_ptr in range(col_len):
            # Check if the coordinate is a land and has not been visited
            if grid[row_ptr][col_ptr] == '1' and (row_ptr, col_ptr) not in visited:
                num_of_islands += 1 # Increment the number of islands
                dfs_isIsland(row_ptr, col_ptr) # Do a dfs traversal on its adjacent cells or coordinates to check if they are also lands and are connected
    return num_of_islands
                
if __name__ == '__main__':
    grid1 = [["1","1","1","1","0"],
              ["1","1","0","1","0"],
              ["1","1","0","0","0"],
              ["0","0","0","0","0"]]
    
    grid2 = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]]
    
    grids = [grid1, grid2]
    for grid in grids:
        print(numIslands(grid))