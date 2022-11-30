# Implementing a Linked List

class Node:
    '''
    Creating a Node class that takes in attrributes;
    val = Anv value of str, int type
    next = pointer or reference to another node (i.e the pointer of one node refers to memory location of another node, Hence linkedlist)
    '''
    
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
        
class LinkedList:
    '''
    Creating a LinkedList with a head
    head =  start of linkedlist
    '''

    def __init__(self):
        self.head = None
                
    
    # method to insert val to the top of a linkedlist
    def pre_insert(self, val):
        # Takes in val - value to be entered in the linkedlist
        
        # To insert val into the linkedlist, we create a node of the val and make its pointer refer to None
        node = Node(val, self.head) # Create a node to be inserted at the top of the LL, the pointer of this node will point to the head of the LL
        self.head = node # Then update the node as the new head of the linkedlist
        
    # Method to insert val at the end of a Linkedlist
    def post_insert(self, val):
        if self.head == None: # If the Linkedlist is empty, we insert the val directly as the head of the Linkedlist
            self.pre_insert(val)
        
        # If LL not empty, we traverse the LL till we get to the end (which is where the pointer of the last node is None) and then insert the val
        temp = self.head # Create a temp variable to start at the top of the linkedlist
        while temp.next: # Traverse the LL until we get to the end
            temp = temp.next # Update the pointer to the next node
        # At this point we got to the end of the LL and now we insert the new val    
        temp.next = Node(val, None)
        
    # Method to insert a list of values
    def insert_values(self, val_list):
        for val in val_list:
            self.post_insert(val)
            
    # Method to get the length of a linkedlist
    def get_len(self):    
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    # Method to insert element at an index
    def insert_at(self, index, val):
         # Check to see that the index is not negative or index is not greater than the length of the list
        if index < 0 or index > self.get_len():
            raise Exception("Invalid index to insert at")
        # If we want to insert val at the first index of the LL
        if index == 0:
            self.pre_insert(val)
            return
        
        # If at all other indices
        count = 0
        temp = self.head # We start at the top of the LL
        while temp: # Trasverse the LL till we get to the element before the one we want to insert and point our next to the one after the element to be removed
            if count == index - 1: # If we are at the index of the element before the one we are about to insert
                node = Node(val, temp.next) # Create a node of the val to be inserted with its pointer/next pointing to the item after
                temp.next = node # Point the current node to the new node inserted.
                break
            temp = temp.next # Update the pointer to the next node
            count += 1 #Update the count
    
    # Method to remove an element at an index
    def remove_at(self, index):
        # Check to see that the index is not negative or index is not greater than the length of the list
        if index < 0 or index > self.get_len():
            raise Exception("Invalid index to remove")
        
        # If we want to remove the index of the first element
        if index == 0:
            self.head = self.head.next # We point the head to the next element (i.e the element that the current head points or refers)
            
        # If at all other indices
        count = 0
        temp = self.head # We start at the top of the LL, create a pointer to traverse the llist
        while temp: # Trasverse the LL till we get to the element before the one we want to remove and point our next to the one after the element to be removed
            if count == index - 1: # If we are at the index of the element before the one we are about to remove
                temp.next = temp.next.next # We point our next to the one after the element to be removed
                break
            temp = temp.next # Update the pointer to the next node
            count += 1 #Update the count
            
            
    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return 
        
        temp = self.head
        llstr = ''
        
        while temp: # While the linkedlist/a node is not None, 
            llstr += str(temp.val) + '-->' # create a string of the val of each node in the linkedlist
            temp = temp.next # update the pointer to the next node
        print(llstr)
        
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.pre_insert(5)
    ll.pre_insert(57)
    ll.pre_insert(200)
    ll.post_insert(54)
    ll.post_insert(0)
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    
    ll.remove_at(7)
    
    ll.print()
    ll.insert_at(0, 'figs')
    ll.print()
    ll.insert_at(7, 'Jack')
    
    ll.print()
    print(ll.get_len())
    ll.print()