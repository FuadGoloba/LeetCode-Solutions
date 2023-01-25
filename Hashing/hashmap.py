# Implementing a hashmap

class Pair:
    '''
        Creating a Key - Value pair object
    '''
    def __init__(self, key, val):
        self.key = key
        self.val = val
        
class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
    
    # method to hash a key and return a hash index
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

    
    
    
        
        
         
        