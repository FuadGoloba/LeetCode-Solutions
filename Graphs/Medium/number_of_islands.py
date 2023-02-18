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
    
    # Creating a bfs algorithm to traverse connected lands to find an island
    def bfs_isIsland(row_ptr, col_ptr):
        """
            A BFS traversal algorithm to traverse adjacent cells (lands) and check if its part of a connected Island
        """
        # Create a queue (FIFO) to keep track of coordinates of adjacent neighbour lands
        queue = collections.deque()
        
        # Updated to include the current coordinate (land) we're at
        visited.add((row_ptr, col_ptr))
        queue.append((row_ptr, col_ptr))
        
        # Traverse every visited land's neighbour to check if they are part of the connected island; 
        # Do that until there are no more neighbouring lands
        while queue:
            row_ptr, col_ptr = queue.popleft() # pop the coordinate of the land at the top of the queue in order to check if they have 
                                               # neighbour/adjacent lands that are also connected to the current island
            
            # Create an array of possible directions to traverse (up, down, left, right)
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            # Initialise the adjacent coordinates based on the direction of traversal
            for r, c in directions:
                adj_row_ptr = row_ptr + r 
                adj_col_ptr = col_ptr + c
                
                # Check if the adjacent coordinates are valid (within bound of the grid) and the coordinate represents a land and has not been visited
                if adj_row_ptr in range(row_len) and adj_col_ptr in range(col_len) and grid[adj_row_ptr][adj_col_ptr] == '1' and (adj_row_ptr, adj_col_ptr) not in visited:
                    queue.append((adj_row_ptr, adj_col_ptr)) # Add the adjacent land to the queue
                    visited.add((adj_row_ptr, adj_col_ptr)) # Add the adjacent lands to the global variable visited
        
    # Traversing the entire grid to find connected islands
    # Note: AN island is a connection of adjacents lands horizontally or vertically
    for row_ptr in range(row_len):
        for col_ptr in range(col_len):
            # Check if the coordinate is a land and has not been visited
            if grid[row_ptr][col_ptr] == '1' and (row_ptr, col_ptr) not in visited:
                bfs_isIsland(row_ptr, col_ptr) # Do a bfs traversal on its adjacent cells or coordinates to check if they are also lands and are connected
                num_of_islands += 1 # Increment the number of islands
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