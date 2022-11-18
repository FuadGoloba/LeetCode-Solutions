# Remove Nth Node from End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

class Node:
    
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def get_len(self):
        length_of_list = 0
        temp = self.head
        while temp:
            temp = temp.next
            length_of_list += 1
        return length_of_list
        
    def removeNthFromEnd1(self, n):
        '''  Time = O(n), Memory = O(n)
            The idea is to get the length of the entire LL and then, the length - n will give us the nth-1 node
            Then we can traverse the list until we get to the nth-1 node and then delete the nth node'''
        
        # First we get the length of the entire LL in order to compute the nth-1 node
        length_of_list = self.get_len()
            
        nth_node = length_of_list - n # Compute index of nth node
        index = 0 #Initilalise to keep track of current index location
        curr = self.head 
        while curr: # Traverse the llist till we get to the index of nth-1 node in order to delete the nth node
            if index == nth_node - 1: # check that we are at the index of nth-1 node
                curr.next = curr.next.next # Delete the nth node and break from the loop
                break
            curr = curr.next
            index += 1
            
    def removeNthFromEnd2(self, n):
        '''
        # using a Dummy node and Two Pointers - Time = O(n), memory = O(n)
        # Using Two pointers, we can shift the left and right pointer by n and traverse till we get to null, the left pointer at this point will be the nth node to be removed
        # But we need to get to the node before the nth node and we can do that by creating a dummy node to be the start of the left pointer and the right pointer is n distance apart from the head of the list
        # Then we keep shifting left and right pointers till right gets to NULL, at this point,left is at nth-1 node and then we can delete the nth node and connect nth-1 node to nth's node next node
        '''
        if self.head == None:
            return 

        dummy = Node(0, next = self.head) # Create dummy node to point to the head
        left_pointer = dummy # Left pointer start at the dummy node so by shifting to the next pointer, we ecventually have the left pointer become to the Nth-1 node

        # To get the initialisation of the right pointer, We need to traverse the list n times starting from the head
        right_pointer = self.head
        while right_pointer and n > 0:
            right_pointer = right_pointer.next
            n -= 1
            
        # Traverse the list until the right pointer is None and here, the Left pointer is as the nth-1 node
        while right_pointer:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
        
        # Deleting the nth node; point the left pointer's next to the nth node's next
        left_pointer.next = left_pointer.next.next
        return dummy.next # Here we return the Linkedlist
    
    
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
            #print("Linked List is empty")
            return None
        
        temp = self.head
        llstr = ''
        
        while temp: # While the linkedlist/a node is not None, 
            llstr += str(temp.val) + '-->' # create a string of the val of each node in the linkedlist
            temp = temp.next # update the pointer to the next node
        print(llstr)
        
        
if __name__ == '__main__':

    for array, nth in [([1,2,3,4,5],1), ([3,7,78, 16],3), ([1,2], 1), ([], 1)]:
        ll = LinkedList()
        ll.append_all(array)
        print(f'Given Linkedlist to remove {nth}th node from end: ')
        ll.print()
        print(f'Linkedlist after removing {nth}th node from end: ')
        ll.removeNthFromEnd1(nth)
        ll.print()

        
        