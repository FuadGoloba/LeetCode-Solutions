# REVERSE A LINKEDLIST

# Given the head of a singly linked list, reverse the list, and return the reversed list. (Try it Iteratively and Recursively)

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

class Node:
    
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = None # Head of list
        
        
    def reverseList1(self):
        '''
            Solving Iteratively using Two pointers; Time = O(n), Memory = O(1)
        '''
        
        prev, curr = None, self.head # Initialise a previous and current pointer; While we travwrse the list, we want to point the pointer of a current node to a previous node thereby reversing it's link
                                     # And then updating the previous to go to the current and the current goes to the next and same thing as above applies
        
        # Traverse the LL until the curr node becomes None
        while curr:
            temp = curr.next # Keep track of the next node before breaking it's link
            curr.next = prev # Make the next node point to the previous
            prev = curr # Update the previous to be the current node
            curr = temp # Update the current node to be the next node
         
        self.head = prev # Mke prev the new head   
        
        return prev # Returns the head of the reversed list; Eventually prev will become the last node before the loop terminates

    
    def reverseList2(self, head):
        '''
            Solving Recursivley by dividing the problem into sub problems and solving; Time = O(n), Memory = O(n)
                1. Divide the llist into 2 parts; first node and rest of the llist
                2. Recurse the rest of the llist
                3. link the rest of the llist to first
                4. Make head pointer point to NULL
        '''
        if not head:
            return None
    
        newHead = head # Initialise a newHead to the last element of each subproblem llist
        
        if head.next:
            newHead = self.reverseList2(head.next) # Recurse the rest of the list; making NewHead become the last element of the list (i.e newHead will always be the last element of any sub problem e.g 1 -> NULL, newHead will recurse to return head which is 1)
                                                    # e.g; 1->2->NULL; newHead will be 1 at the start and will recurse and finally become 2
            head.next.next = head # Reverse the list making the next node point to the previous (e.g with 1->2; at head = 1, head.next = 2, then head.next.next = head; means the pointer at node(2) will reverse point to node 1)
            head.next = None # Mkae head pointer point to NULL (i.e 2 -> 1 -> NULL)
            
        return newHead # Return the newHead
    
    
    def append(self, val):
        
        if self.head == None:
            self.head = Node(val, None)
            return
            
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val, None)
        
    def append_all(self, array):
        for val in array:
            self.append(val)
    
    def print(self):
        
        if self.head == None:
            print('LinkedList is empty')
            return 
        
        ll_str = ''
        
        temp = self.head
        while temp:
            ll_str += str(temp.val) + '-->'
            temp = temp.next
        print(ll_str)
        

if __name__ == '__main__':

    for array in [[1,2,3,4,5], [1,3,7,78], [1,2], []]:
        ll = LinkedList()                                                                                                   
        ll.append_all(array)
        print('Given Linkedlist: ')
        ll.print()
        print('Reversed Linkedlist: ')
        ll.head = ll.reverseList2(ll.head)
        ll.print()

    