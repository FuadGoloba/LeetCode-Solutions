#Product of array Except Itself {MEDIUM}
#   Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#   The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#   You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

def productExceptSelf1(nums):
    '''
        Using arrays to compute prefixes and suffixes; Time = O(n), Memory = O(n)
    ''' 
    prefix = [0] * len(nums) # Create a prefix of products of all elements up to an index position
    suffix = [0] * len(nums) # Create a suffix of product of all elements after an index position
    product = [0] * len(nums) # Array to store product of prefix and suffix at an index position
    
    # Compute the Prefix 
    prefix[0] = 1 # Prefix of first element has to be 1
    for i in range(1, len(nums)): # Traverse the array starting at the second element
        prefix[i] = prefix[i - 1] * nums[i - 1] # Prefix at an index position is product of previus fix and previous element in the array
    
    # Compute the Suffix
    suffix[len(nums) - 1] = 1 # Suffix of last element has to be 1
    for j in range(len(nums) - 2, -1, -1): #Traverse the array from the second last position up to the 0th index
        suffix[j] = suffix[j + 1] * nums[j + 1] # Suffix at an inde3x position is the product of next suffix already computed and element at that index
        
    # COmpute the Product of array except itself
    for n in range(len(nums)):
        product[n] = prefix[n] * suffix[n]
                
    return product


def productExceptSelf2(nums):
    '''
        Computing the product of the array  without using any extra space; Time = O(n), Memory = O(1)
    '''
    
    product = [1] * len(nums)
    
    # First computing the prefix of each element and storing in the result array
    prefix = 1
    for i in range(len(nums)): # Traverse each element in the array and in each tail position, input the prefix (i.e product of previous prefix and previous element in the array)
        product[i] = prefix # the prefix at an index is the product of previous prefix and previous element in the array
        prefix *= nums[i] 
        
    suffix = 1
    for i in range(len(nums) - 1, -1, -1): # Traverse the elements in the array from the last element up to the start, multiply the suffix by the prefix already in the result array
        product[i] *= suffix # the result at an index is the product of it's prefix and suffix
        suffix *= nums[i]
    return product
        
if __name__ == '__main__':
    for arr in [[1,2,3,4], [-1,1,0,-3,3]]:
        print(productExceptSelf2(arr))
