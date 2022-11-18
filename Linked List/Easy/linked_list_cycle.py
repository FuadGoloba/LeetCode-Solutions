# LINKED LIST CYCLE

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

from reverse_linked_list import Node, LinkedList

# class Node:
    
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next
        
class Cycle(LinkedList):
        
    def hasCycle(self):
        '''
            Using a hashset, Time = O(n), Memory = O(n)
        '''
        # Traverse the list one by one and keep putting the node addresses in a Hash Table. 
        # At any point, if NULL is reached then return false, and if the next of the current nodes points to any of the previously stored nodes in  Hash then return true.
        
        seen_nodes = set()
        curr = self.head
        
        while curr:
            if curr.next in seen_nodes: # Check if the current node points to a previously stored node in the hashset 
                return True
            else:
                seen_nodes.add(curr) # Add visited nodes in the hashset
            curr = curr.next
        return False
    

if __name__ == '__main__':
    for array in [[3,2,0,-4]]:
        ll = Cycle()
        ll.append_all(array)
        print('Given LinkedList: ')
        ll.print()
        
        ll.head.next.next.next.next = ll.head
        print(ll.hasCycle())
    
    
        