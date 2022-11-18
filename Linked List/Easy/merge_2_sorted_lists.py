# Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

class Node:
    
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    
    def mergeTwoLists(self, list1, list2):
        
        # Create a Dummy node; a temporary dummy node as the start of the result list. 
        # The pointer Tail always points to the last node in the result list, so appending new nodes is easy. 
        # The dummy node gives the tail something to point to initially when the result list is empty. This dummy node is efficient, since it is only temporary, and it is allocated in the stack. 
        # The loop proceeds, removing one node from either ‘list1’ or ‘list2’, and adding it to the tail. When We are done, the result is in dummy.next. 
        dummy = Node(0)
        tail = dummy
        
        # Traverse both lists making sure that both are not none
        while list1 and list2:
            if list1.val < list2.val: # Compare the items in both lists and enter the smallest into the tail list
                tail.next = list1 # enter the smallest into the tail list
                list1 = list1.next # update the traversal on list1 to go to the next item
            else:
                tail.next = list2 # If the item in list 2 is bigger or are equal, enter the item into the result list and update the traversal on list2 to go to the next item
                list2 = list2.next
            tail = tail.next # After comparing and entering the values into the tail list, we want to also update result 
            
        # Check that we have gotten to the end of the list and there are values in one of the lists that remain
        if list1: # If list1 still has values
            tail.next = list1 # point the end of the tail to the remaining values of list 1
        elif list2: # if list 2 still has values
            tail.next = list2 # Point the end of the tail to the remaining values of list2
            
        return dummy.next # Return the head of the merged list

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
            print('Linked List is empty')
            return 
        
        ll_str = ''
        temp = self.head
        while temp:
            ll_str += str(temp.val) + '-->'
            temp = temp.next
        print(ll_str)
    
                
if __name__ == '__main__':

    for lis1, lis2 in [([1,2,4],[1,3,4]), ([1,4,5], [1,3,6]), ([], [1])]:
        ll = LinkedList()
        list1 = LinkedList()
        list2 = LinkedList()
        list1.append_all(lis1)
        list2.append_all(lis2)
    
        print('Given Linkedlist: ')
        list1.print()
        list2.print()
        print('Merged LinkedList: ')
        ll.head = ll.mergeTwoLists(list1.head, list2.head)
        ll.print()
    