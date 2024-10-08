# Static Array

import ctypes

class StaticArray(object):
    def __init__(self, capacity):
        self.n = 0
        self.capacity = capacity
        self.arr = self.make_array()
        
    def make_array(self):
        """Creates an Array"""
        return (self.capacity * ctypes.py_object)()
    
    def __len__(self):
        """Returns the length of the Array or number of items in the array

        """
        return self.n
    
    def __getitem__(self, index: int):
        """Retrieves the item at a given index of the Array

        Args:
            index (_int_): Index to retrieve item from Array

        Raises:
            IndexError: Index is out of bounds

        Returns:
            _int_: item at given indnex
        """
        if index >= self.capacity or index < 0:
            raise IndexError('Index is out of bounds')
        try:
            return self.arr[index]
        except:
            return None
    
    def append_(self, n):
        """Append to the Array

        Args:
            n (_int_): Integer to append to the Array

        Raises:
            MemoryError: No space to accomodate new item or integer
        """
        if self.n == self.capacity:
            raise MemoryError('Array capacity is full')
        
        self.arr[self.n] = n
        self.n += 1
        
    def insert_(self, n:int, index:int):
        """Insert an integer at an index without replacing the existing integer

        Args:
            n (_int_): Integer to insert into the Array
            index (_int_): Index of Array to insert at

        Raises:
            MemoryError: Array capacity is full
        """
        if self.n == self.capacity:
            raise MemoryError('Array capacity is full')
        
        if self.__getitem__(index) and self.__getitem__(index - 1):
            for i in range(self.n, index, -1):
                self.arr[i] = self.arr[i - 1]
            self.arr[index] = n
            self.n += 1
        elif self.__getitem__(index - 1) and not self.__getitem__(index):
            self.append_(n)
            
    def print_arr(self):
        """Print the Array

        Returns:
            _str_: A list representation of the array
        """
        array = "["
        for i in range(self.n):
            # print(self.arr[i])
            array += str(self.arr[i]) + ','
        array += "]"
        return array
            
if __name__ == '__main__':
    print("Create a static array of size 5")
    arr = StaticArray(5)
    print(f"Append 2 integers to array of capacity {arr.capacity}")
    for i in range(2):
        arr.append_(i)
        
    print(f"Array has {len(arr)} items currently")
    print(f"The integers currently in the array are; \n{arr.print_arr()}")
    print('------')
    print(f"Append an integer to array of capacity {arr.capacity}")
    arr.append_(3)
    print(f"Array has {len(arr)} items currently")
    print(f"The integers currently in the array are; \n{arr.print_arr()}")
    print('------')
    print("Insert an integer at index 2 of the array")
    arr.insert_(2, 2)
    print(f"Array has {len(arr)} items currently")
    print(f"The integers currently in the array are; \n{arr.print_arr()}")             
        