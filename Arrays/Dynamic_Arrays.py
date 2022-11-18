# Implementing a Dynamic Aarray

import ctypes # Built in library used to create a raw array

class DynamicArray(object):
    
    def __init__(self):
        self.n = 0 # instantiate the count of the array to be 0 (i.e an empty array at start)
        self.capacity = 1 # The Dynamic array has a capacity of 1 at start
        self.arr = self.make_array(self.capacity) # Create the dynamic array
        
    # Method to make an array given a capacity
    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
    
    # Nethod to return the size of the array
    def __len__(self):
        return self.n
    
    # Method to get an element/item at an index
    def __getitem__(self, index):
        # Check that the index isn't out of range of the count of elements in the array
        if not 0 <= index < self.n:
            return IndexError('Index is out of bounds!')
        
        return self.arr[index]
    
    def append(self, item):
        
        # Resize the array if capacity is maxed
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        
        # Append the element to the array
        self.arr[self.n] = item
        self.n += 1
        
    # Method to resize array
    def _resize(self, new_cap):
        
        # Allocate a new array with larger capacity
        new_array = self.make_array(new_cap)
        
        # make the new array refer to elements of the old array
        for index in range(self.n):
            new_array[index] = self.arr[index]
        
        # Set the arr to be the new array and increment its capacity 
        self.arr = new_array
        self.capacity = new_cap


if __name__ == '__main__':
    
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)      
        
    print(len(arr))
        