# Count the unique paths from source to destination. 

# Given a grid/matrix, count the unique paths from the top left to the bottom right.
# Note that a single path only move along 0s and can't visit the same cell more than once. So 1 represents block and 0 represents a pass


def findPathsDFS(grid, row_pointer, col_pointer, visited):
    '''
        Using DFS (backtracking); Time complexity -> O(4^(n*m)) cause we brute-force by going through all possible coordinates that can lead to a path
                   Space complexity -> 0(n*m)
        
        Idea is to find the initial uniique path by going through all possible coordinates possible(available) till we get to the destination, and then backtrack to find another potential unique path
    '''
    # Get the length of the rows and cols in the matrix 
    row_len, col_len = len(grid), len(grid[0])
    
    
    # Base Case
        # Setting conditions to spot traversals that don't lead to a path
            # Check if we're outside of the matrix (on the -ve axes)
            # Check if we're outside of the matrix (on the +ve axes)
            # Check if the coordinate has been visited
            # Check if it's a blocked coordinate (i.e a 1)
    if min(row_pointer, col_pointer) < 0 \
        or row_pointer == row_len or col_pointer == col_len \
        or (row_pointer, col_pointer) in visited \
        or grid[row_pointer][col_pointer] == 1: 
        return 0
    
        # Condition for when we find a path that has led to the destination
    if row_pointer == row_len - 1 and col_pointer == col_len - 1:
        return 1
    
    # Add the coordinates to visted coordinates
    visited.add((row_pointer, col_pointer))
    
    # Initialise a counter to count unique paths
    count = 0
    
    # Recursively traverse all possible cooordinates from the present location (i.e up, down, left, right)
    count += findPathsDFS(grid, row_pointer - 1, col_pointer, visited)
    count += findPathsDFS(grid, row_pointer + 1, col_pointer, visited)
    count += findPathsDFS(grid, row_pointer, col_pointer - 1, visited)
    count += findPathsDFS(grid, row_pointer, col_pointer + 1, visited)
    
    # Once we get to the destination, we backtrack (now starting from the destination to the source) to find if alternative paths could have led to the destination
    # So we remove coordinated that have been visited in order to backtrack
    visited.remove((row_pointer, col_pointer))
    return count
    
if __name__ == '__main__':
    matrix = [[0,0,0,0],
              [1,1,0,0],
              [0,0,0,1],
              [0,1,0,0]]
    visited = set()

    print(findPathsDFS(matrix, 0, 0, visited))
    
