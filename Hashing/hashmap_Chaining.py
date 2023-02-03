# Implementing a hashmap/ HashTable using Separate Chaining Method

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

class Pair:
    '''
        Creating a Key - Value pair object
    '''
    def __init__(self, key, val):
        self.key = key
        self.val = val
        
class HashMap:
    '''
        Creating a Hashmap
    '''
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
    
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
    
    # method to get or retrieve a key from the Hashmap/ Hashtable
    def get(self, key):
        ''' Using Separate Chaining method'''    
        index = self.hash(key) # Get the hash index of the key
        
        # Check that the hash index is not empty
        if self.map[index] != None:
            for k in self.map[index]: # Iterate the entire chain at the hash index to find the key
                if k.key == key:
                    return k.val # return its value if exists
        return None # Should the key not exist
    
    
    # method to insert a Key-Value pair
    def put(self, key, val):
        
        index = self.hash(key) # Get the hash index of the key
        
        # Case chain does not exist yet at that index; Create a chain and add the Key-Value pair
        if self.map[index] == None:
            self.map[index] = [Pair(key, val)]
            self.size += 1 # Update the size of the array
            if self.size >= self.capacity // 2:
                self.rehash() # Rehash the hashmap by doubling its size and hashing its elements again
            return
            
        # Case when a chain exists
        elif self.map[index] != None:
            # Case Key does not exist in the chain
            if self.get(key) == None:
                self.map[index].append(Pair(key, val)) # append the new pair to the chain
                return
            
            # Case Key exists in the chain
            else:
                for idx, k in enumerate(self.map[index]):
                    if k.key == key:
                        self.map[index][idx] = Pair(key, val) # Overwrite the pair with the new value
                        return
                    
    # method to rehash a hashmap/ hashtable as soon as the total chain in the hash table is half the size of the hashtable
    def rehash(self):
        
        self.capacity = 2 * self.capacity # Doubling the size of the hashmap
        newHashMap = [None for i in range(self.capacity)] # Create a new Hashmap array with the new capacity
        
        oldHashMap = self.map # initialise a temporaray variable to store the current elements in the hashmap
        self.map = newHashMap # Initialising a new Hashmap
        self.size = 0 # Set the initial size of the Hashmp to be 0
        
        # Inserting elements from Old Hashmap into New Hashmap
        for chain in oldHashMap:
            if chain != None:
                for pair in chain:
                    self.put(pair.key, pair.val)
    
    # print hashmap/hashtable
    def print(self):
        for chain in  self.map:
            if chain != None:
                for pair in chain:
                    print(pair.key, pair.val)  

                
    
if __name__ == '__main__':
    
    pairList = [('Fuad', 1), ('Koko', 2), ('Goloba', 3), ('Kay', 4)]
    # Initialising a Hashmap object
    NameMap = HashMap()
    # Inserting key-value pair into hashmap
    for pair in pairList:
        NameMap.put(pair[0], pair[1])
    
    # Retreiving values from the hashmap
    print(NameMap.get('Kay'))
    print(NameMap.get('Boj'))
    
    print('\nThe hashmap contains the following elements:')
    NameMap.print()

    
    
    
        
        
         
        