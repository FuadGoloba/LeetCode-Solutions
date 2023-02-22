# Length of shortest Path in a 4-directionally connected Binary Matrix

# Given an n x n binary matrix grid, return the length of the shortest path from top left of the grid to the bottom right in the matrix. If there is no path, return -1.

# A path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# You can only move horizontally and vertically
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 4-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

import collections

def lengthShortestPathBinaryMatrix(grid):
    """
        Using BFS algorithm for traversal : Time - O(n*m); Space - O(n*m)
        BFS is more efficient since the first time a vertex is discovered during the traversal, the distance from our source would give us the shortest path 
    """
    # Get the length of the rows and columns in the matrix/grid
    row_len, col_len = len(grid), len(grid[0])
    
    visited = set() # Hashset to keep track of the visited coordinates/vertex
    queue = collections.deque() # Queue (FIFO) to keep track of neighbouring coordinates with potential to traverse
    
    # Add the initial coordinates to the queue and visted hashset
    queue.append((0, 0))
    visited.add((0, 0))
    
    length_of_path = 0
    
    while queue:
        for vertex_idx in range(len(queue)):
            row_ptr, col_ptr = queue.popleft() # pop the coordinates of the current neighbours at the top of the queue in order to check if they have 
                                               # neighbours that may continue the path to destination
            # Check if we have arrived at the destination                                               
            if row_ptr == row_len - 1 and col_ptr == col_len - 1:
                return length_of_path
            
            # Create an array of possible directions to traverse (up, down, left, right)
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                neighbour_row_ptr = row_ptr + dr
                neighbour_col_ptr = col_ptr + dc

            # Setting conditions to spot traversals that don't lead to a path so we skip them and go to the next available direction
                # Check if we're outside of the matrix (on the -ve axes)
                # Check if we're outside of the matrix (on the +ve axes)
                # Check if the coordinate has been visited
                # Check if it's a blocked coordinate (i.e a 1)                
                if (min(neighbour_row_ptr, neighbour_col_ptr) < 0
                    or neighbour_row_ptr == row_len
                    or neighbour_col_ptr == col_len
                    or (neighbour_row_ptr, neighbour_col_ptr) in visited
                    or grid[neighbour_row_ptr][neighbour_col_ptr] == 1
                    ):
                    continue
                # If there are valid neighbours, then we add them to the queue and visited
                queue.append((neighbour_row_ptr, neighbour_col_ptr))
                visited.add((neighbour_row_ptr, neighbour_col_ptr))
        
        # Increment the length of the path
        length_of_path += 1
    return -1


if __name__ == '__main__':
    grid1 = [[0,1],[1,0]]
    grid2 = [[0,0,0],[1,1,0],[1,1,0]]
    grid3 = [[1,0,0],[1,1,0],[1,1,0]]
    grid4 = [[0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]]
    
    grids = [grid1, grid2, grid3, grid4]
    #grids = [grid4]
    for grid in grids:
        print(lengthShortestPathBinaryMatrix(grid))
        

                    
    