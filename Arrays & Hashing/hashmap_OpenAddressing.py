# Implementing a hashmap/ HashTable using Open Addressing Method

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

# IMPLEMENTATION USING LINEAR-PROBING OPEN ADDRESSING
    # In open addressing, all elements are stored in the hash table itself. Each table entry contains either a record or NIL. 
    # When searching for an element, we examine the table slots one by one until the desired element is found or it is clear that the element is not in the table.
    # In linear probing, the hash table is searched sequentially that starts from the original location of the hash. If in case the location that we get is already occupied, then we check for the next location. 
    # The limitation here however is that the total number of entries in the table is limited by the size of the array.
    

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
        ''' Using Linear probing Open Addressing Collision Handling method'''    
        
        index = self.hash(key) # Get the hash index of the key

        # Iterate until we find an empty hash index (meaning that the key does not exist)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1 # We check the next closest index as per Linear Probing Open Addressing COllision handling method
            index = index % self.capacity # Mod the index by the capacity to ensure that we don't get out of bounds of the capacity
            
        return None # Should the key not exist
                
    # method to insert a Key-Value pair
    def put(self, key, val):
        index = self.hash(key)
        
        while True:
            # Case when the Key does not already exist in the hash table and its hash index is empty 
            if self.map[index] == None:
                self.map[index] = Pair(key, val) # Insert the Key-Value pair to the posn of the empty index
                self.size += 1 # update the size of the array
                if self.size >= self.capacity // 2:
                    self.rehash()
                return 
            # Case when the key already exists, we try to overwrite its old value with the new value
            elif self.map[index].key == key:
                self.map[index].key = val # Overwrite the value if the key exists
                return 
            
            index += 1 # We check the next closest index as per Linear Probing Open Addressing COllision handling method
            index = index % self.capacity # Mod the index by the capacity to ensure that we don't get out of bounds of the capacity
    
    # method to rehash a hashmap/ hashtable
    def rehash(self):
        
        self.capacity = 2 * self.capacity # Doubling the size of the hashmap
        newHashMap = [None for i in range(self.capacity)] # Create a new Hashmap array with the new capacity
        
        oldHashMap = self.map # initialise a temporaray variable to store the current elements in the hashmap
        self.map = newHashMap # Initialising a new Hashmap
        self.size = 0 # Set the initial size of the Hashmp to be 0
        
        # Inserting elements from Old Hashmap into New Hashmap
        for pair in oldHashMap:
            if pair:
                self.put(pair.key, pair.val)
                
    # print hashmap/hashtable
    def print(self):
        for pair in self.map:
            if pair:
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

    
    
    
        
        
         
        