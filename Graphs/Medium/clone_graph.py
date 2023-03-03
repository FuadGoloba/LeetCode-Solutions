# Clone Graph

# Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
    # class Node {
    #     public int val;
    #     public List<Node> neighbors;
    # }
 
# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. 
# The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

# DFS technoque to clone a node     
def cloneGraphDFS(node):
    '''
        Using DFS traversal - Time complexity - O(n) where n is (E + V) ie (number of edges + number of vertices of the graph)
                              Space Complexity - O(n)
    '''
    
    origToClone = {} # Hashmap to track nodes that have been cloned

    # DFS to clone a node
    def clone_node(node):
        # Base case - if we have cloned a node, we return its clone
        if node in origToClone:
            return origToClone[node]
        
        # Create a clone if the node hasn't been cloned before and add to the hashmap
        cloned = Node(node.val)
        origToClone[node] = cloned

        # Run DFS on the neighbours of the node to recursively clone them
        for neighbor in node.neighbors:
            cloned.neighbors.append(clone_node(neighbor)) # clone the neighbors of the node

        return cloned
    
    return clone_node(node) if node else None

# BFS technique to clone a node
def cloneGraphBFS(node):
    '''
        BFS to clone a node
    '''
    from collections import deque
    origToClone = {} # Hashmap mapping nodes to their clone to keep track of cloned nodes
    queue = deque # QUeue to traverse neighbor nodes
    
    # Should a node not exist
    if not node:
        return None
    
    cloned =  Node(node.val) # Create a clone of the first node
    queue.append(node) # add the first node to the queue
    origToClone[node] = cloned # Add the cloned node to the hashmap
    
    # Traversing the queue of neighbor nodes
    while queue:
        curr = queue.popleft() # Get the current node from the queue
        # Traverse the list of its neighbors should a node have neighbors that haven't been cloned
        for neighbor in node.neighbors:
            if neighbor not in origToClone: # Should the neighbor node not have been cloned, clone and include in the hashmap
                queue.append(neighbor) # add to the queue to traverse its neighbors next
                cloned = Node(neighbor.val) # clone the current neighbor
                origToClone[neighbor] = cloned # add the cloned neighbor to the hashmap
            origToClone[curr].neighbours.append(origToClone[neighbor]) # add the cloned neighbour to the current nodes' list of neighbors
    
    
    return origToClone[node]        
    
    
    

