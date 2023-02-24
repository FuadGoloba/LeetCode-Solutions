# Count the unique paths from source to destination. 

# Given directed edges to build an adjacency list, count the number of unique paths from a given source to destination


# Building an adjacency list
def construct_adj_list(edges):
    
    adj_list = {} # Using a hasmap to build an adjacency list where the key is a vertex and it maps to a list of its neighbors, which are also vertices. 
    # A hash map works here because we are assuming that all of the values keys are unique.
    
    # Loop through list of edges and map vertices to their neighbours
    for src, dest in edges:
        if src not in adj_list: 
            adj_list[src] = [] # Create a vertex for the source if it doesn't already exist
        if dest not in adj_list:
            adj_list[dest] = [] # Create a vertex for the destination if it doesn't already exist and its neighbours can be empty meaning that it doesn't connect to any other vertex
        adj_list[src].append(dest) # Add the destination vertex as a neighbour of that source
        
    return adj_list


# Creating a DFS algorithm (backtracking) to find the number of unique paths from source to destination
def findPathDFS(node, dest_node, adj_list, visited):
    """_summary_

    Args:
        node (char): source node
        dest_node (char): destination node
        adj_list (Dict): Hashmap representing adjacency List
        visited (Set): Hashset for keepong track of visited nodes

    Returns:
        int: number of unique paths found
        
    Time Complexity = O(n^v) where n is the number of edges and v the number of vertices. This is inefficiecnt compared to BFS
    Space Complexity = O(v)
    """
    
    # Base case
    if node in visited: # We don't want to count nodes that have been visited more than once
        return 0
    if node == dest_node: # We have reached the destination and can backtrack to the source
        return 1
    
    # Initialise a counter for the number of paths found
    no_of_path = 0
    
    # Add the node to the list of visited
    visited.add(node)
    
    # Recursively find paths by traversing the neighbour nodes until destination is reached after which we return 1 as we have found a path and then backtrack to find alternative paths
    for neighbour in adj_list[node]:
        no_of_path += findPathDFS(neighbour, dest_node, adj_list, visited)
    # Once we find a path, we backtrack by removing nodes from the visited map
    visited.remove(node)
    
    return no_of_path


def findPathBFS(node, dest_node, adj_list, visited):
    from collections import deque
    """_summary_

    Args:
        node (char): source node
        dest_node (char): destination node
        adj_list (Dict): Hashmap representing adjacency List
        visited (Set): Hashset for keepong track of visited nodes

    Returns:
        int: number of unique paths found
        
    Time Complexity = O(V + E) where E is the number of edges and V the number of vertices. Much better algorithm than the DFS
    Space Complexity = O(v)
    """
    
    no_of_path = 0
    queue = deque() # temporary queue (FIFO) to store neigbouring nodes for traversal
    
    # Add the first node to both the temporary queue and visited hashset to start the BFS traversal
    queue.append(node)
    visited.add(node)
    
    # Traversing the stored nodes to check if their neighbours lead to a path
    while queue:
        for idx in range(len(queue)):
            curr_node = queue.popleft() # popping the first node in the queue in order to traverse its neighbours
            if curr_node == dest_node: # If we reach the destinatiion, we return the no of unique paths so far
                return no_of_path
        
        # Traverse the neighbours of the current node
        for neighbour in adj_list[curr_node]:
            if neighbour not in visited: # çheck that the neigbour has not been visited else we skip it
                visited.add(neighbour)
                queue.append(neighbour)
        # Add to the number of paths at each level (breadth) till we find the destination
        no_of_path += 1
        
    return no_of_path
            

if __name__ == '__main__':
    edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
    adj_list = construct_adj_list(edges)
    
    print(findPathDFS('A', 'E', adj_list, set()))
    print(findPathBFS('A', 'E', adj_list, set()))

    
    
    
    