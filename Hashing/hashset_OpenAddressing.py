# Implementing a hashset/ HashTable using Open Addressing Method

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


class MyHashSet:
    
    def __init__(self):
        self.set = [None, None]
        self.size = 0
        self.capacity = 2

    def hash(self, key):
        if isinstance(key, str):
            index = 0
            for char in key:
                index += ord(char)
            return index % self.capacity
        else:
            return key % self.capacity
        
    def rehash(self):
        self.capacity = 2 * self.capacity
        newSet = [None for i in range(self.capacity)]

        oldSet = self.set
        self.set = newSet
        self.size = 0

        for key in oldSet:
            if key:
                self.add(key)

    def add(self, key: int) -> None:
        index = self.hash(key)

        while True:
            if self.set[index] is None:
                self.set[index] = key
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            #elif self.set[index] is not None:
            elif self.set[index] == key:
                return 
            index += 1
            index = index % self.capacity
            
    
    def contains(self, key: int) -> bool:
        index = self.hash(key)

        while self.set[index] != None:
            if self.set[index] == key:
                return True
            index += 1
            index %= self.capacity
            
        return False

    
    # Method to remove a key from a hashet
    # Note that this done with Open addressing method leads to a bug as we create a hole in the set and the contains() may return False stopping the search early.
    # For example, if we first add 3 at index posn 1 and then try to add 5 (knowing that 5 gives us same index posn 1 but with open addressing will shift to the next available posn; say posn 2)
    # Let's now remove 3 which was initially added (this creates a None in index posn 1). So if we try to use contains() to check if 5 exists in the hashset; we will get a False
    # as it will check the initial hash index posn of 5 (which happens to be index posn 1) but is now None thus stopping our search early. Whereas 5 does exist in the hashset in index posn 2
    # An alternative solution which is bug free is to rehash the table everytime we remove a key but this will turn out to be costly in terms of time complexity
    def remove(self, key: int) -> None:
        ''' Using the bug free but yet expensive solution'''
        if self.contains(key) == False:
            return
        
        index = self.hash(key)

        while True:
            if self.set[index] == key:
                self.set[index] = None
                self.size -= 1
                self.rehash() # Bug free solution
                return 

            index += 1
            index %= self.capacity
        

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
    
    
  
    
    
    
