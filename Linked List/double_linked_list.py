class Node:
    '''
    Creating a Node class that takes in as attrributes;
    val = Anv value of str, int type
    prev = pointer to the previous node
    next = pointer or reference to another node (i.e the pointer of one node refers to memory location of another node, Hence linkedlist)
    '''
    
    def __init__(self, prev=None, val=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next

        
class DoublyLinkedList:
    '''
    Creating a Doubly LinkedList with a head
    head =  start of linkedlist
    '''
    
    def __init__(self):
        self.head = None
        
    # Insert at the top of the DLL    
    def pre_insert(self, val):
        
        new_node = Node(None, val, self.head) # Initilaise a node to point to the current head, setting its previous node to NOne since it's going to be the new head            
        self.head = new_node # Set the new node as the new head of the DLL
        

    # Insert at the end of the DLL / Append to the DLL
    def post_insert(self, val):
        
        # CIf the DLL is empty, then we insert at the top
        if not self.head:
            self.pre_insert(val)
            return
         
        # Traverse till the end of the DLL, set the curr node to point to the new node and the new node point to the previous node   
        curr = self.head
        while curr.next:
            curr = curr.next
                
        curr.next = Node(prev=curr,val=val,next=None)
        
    # Insert after a given node of the DLL        
    def insert_after(self, prev_node, val):
        
        # INitialise the new node
        new_node = Node(None,val,None)
        
        new_node.next = prev_node.next # Point the new node to the given node's next node
        prev_node.next = new_node # change the pointer of the given node to point to the new node
        new_node.prev = prev_node # Point the new node to the given node
        
        # CHeck that the node after the given node is not null and point its node to the new node as well
        if new_node.next:
            new_node.next.prev = new_node
    
    
    # Remove from begining of DLL
    def remove_front(self):
        
        # Linked List is empty
        if not self.head:
            print('Linked List is empty')
            return
        
        # Just one item in the Linked List
        if not self.head.next:
            self.head = None
        
        # More than one item in the DLL
        self.head.next.prev = None
        self.head = self.head.next
        
    
    # Remove last element from the DLL    
    def remove_end(self):
        # Linked List is empty
        if not self.head:
            print('Linked List is empty')
            return
        
        # Just one item in the Linked List
        if not self.head.next:
            self.head = None
        
        # Traverse till the end of DLL and remove last element            
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.prev.next = None
         
    def print(self):

        if self.head == None:
            print("Linked List is empty: []")
            return 
        
        curr = self.head
        dll_str = ''
        
        while curr:
            dll_str += str(curr.val) + '<-->'
            curr = curr.next
            
        print(dll_str)
        
if __name__ == '__main__':
    dll = DoublyLinkedList()
    print('Printing Empty Doubly Linked List: ')
    dll.print()
    
    print('Inserting at the top of Doubly Linked List')
    dll.pre_insert(3)
    dll.pre_insert(5)
    dll.pre_insert(57)
    dll.pre_insert(200)
    dll.print()
    
    print('Inserting at the end of Doubly Linked List')
    dll.post_insert(54)
    dll.post_insert(0)
    dll.print()
    
    print('Inserting after the 3rd node of the Linked List')
    node_3 = dll.head.next.next
    dll.insert_after(node_3, 2)
    dll.print()
    
    print('Remove the front of the linkedlist:')
    dll.remove_front()
    dll.print()
    
    print('pop/remove end of the DOubly Linked List')
    dll.remove_end()
    dll.print()
    
        
        
        
        
            
                
        