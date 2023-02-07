# Implementing a hashset/ HashTable using Separate Chaining Method

# Hashing is a technique or process of mapping keys, and values into the hash table by using a hash function. It is done for faster access to elements. 
# The efficiency of mapping depends on the efficiency of the hash function used.
# Let a hash function H(x) maps the value x at the index x%10 in an Array. For example if the list of values is [11,12,13,14,15] it will be stored at positions {1,2,3,4,5} in the array or Hash table respectively.

# HASH FUNCTION
    # The hash function creates a mapping between key and value, this is done through the use of mathematical formulas known as hash functions. The result of the hash function is referred to as a hash value or hash. 
    # The hash value is a representation of the original string of characters but usually smaller than the original.
    # For example: Consider an array as a Map where the key is the index and the value is the value at that index. 
    # So for an array A if we have index i which will be treated as the key then we can find the value by simply looking at the value at A[i]. simply looking up A[i]. 

# PROBLEM WITH HASHING (COLLISION)
    # The hashing process generates a small number for a big key, so there is a possibility that two keys could produce the same value. The situation where the newly inserted key maps to an already occupied, 
    # and it must be handled using some collision handling technology; 
                                # Open Addressing
                                # Separate Chaining

# IMPLEMENTATION USING SEPARATE CHAINING
    # The idea is to make each cell of the hash table point to a linked list of records that have the same hash function value (i.e so that multiple key-value pairs can be stored at the same index.).
    # Chaining is simple but requires additional memory outside the table. In this case, the time complexity comes down to O(n), for searching, inserting and deleting. 
    # This way, any future keys that belong to the same index will be stored as a node in the linked list chain.
        
class MyHashSet:
    '''
        Creating a Hashset
    '''
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.set = [None, None]
    
    # method to hash a key and return a hash index (Hash function)
    def hash(self, key):
        # if the key is a str, then use the sum of it ASCII characters to compute its hash index
        if isinstance(key, str):
            index = 0
            for c in key:
                index += ord(c)
            return (index % self.capacity)
        
        # if it's a digit or numeric value
        else:
            return key % self.capacity
    
    # method to get or retrieve a key from the Hashset/ Hashtable
    def contains(self, key):
        ''' Using Separate Chaining method'''    
        index = self.hash(key) # Get the hash index of the key
        
        # Check that the hash index is not empty
        if self.set[index] != None:
            for k in self.set[index]: # Iterate the entire chain at the hash index to find the key
                if k == key:
                    return True # return its value if exists
        return False # Should the key not exist
    
    
    # method to insert a Key-Value pair
    def add(self, key):
        
        index = self.hash(key) # Get the hash index of the key
        
        # Case chain does not exist yet at that index; Create a chain and add the Key
        if self.set[index] == None:
            self.set[index] = [key]
            self.size += 1 # Update the size of the array
            if self.size >= self.capacity // 2:
                self.rehash() # Rehash the hashset by doubling its size and hashing its elements again
            return
            
        # Case when a chain exists
        elif self.set[index] != None:
            # Case Key does not exist in the chain
            if self.contains(key) == False:
                self.set[index].append(key) # append the new key to the chain
                return
            
            # Case Key exists in the chain
            else:
                return
    
    # Method to remove a key from a hashset
    def remove(self, key):
        index = self.hash(key)
        
        # Check that the key exists otherwise do nothing
        if self.contains(key) == False:
            return
        
        # case the key exists
        else:
            # Iterate the chain to find the key and remove it
            for idx, k in enumerate(self.set[index]):
                if k == key:
                    self.set[index][idx] = None
                    return
                    
    # method to rehash a hashset/ hashtable as soon as the total chain in the hash table is half the size of the hashtable
    def rehash(self):
        
        self.capacity = 2 * self.capacity # Doubling the size of the hashset
        newHashset = [None for i in range(self.capacity)] # Create a new Hashset array with the new capacity
        
        oldHashset = self.set # initialise a temporaray variable to store the current elements in the hashset
        self.set = newHashset # Initialising a new Hashset
        self.size = 0 # Set the initial size of the Hashmp to be 0
        
        # Inserting elements from Old Hashset into New Hashset
        for chain in oldHashset:
            if chain != None:
                for key in chain:
                    if key != None:
                        self.add(key)
    

                
    
if __name__ == '__main__':
    
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    print(obj.contains(1)) 
    print(obj.contains(3))
    obj.add(2)
    print(obj.contains(2))
    obj.remove(2)
    print(obj.contains(2))


    
    
    
        
        
         
        