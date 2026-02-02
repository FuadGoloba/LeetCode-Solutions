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
    Computes the product of the array except itself using separate prefix and suffix arrays.
    
    Intuition:
        For each index, calculate the product of all elements to its left (prefix) and all elements to its right (suffix).
        Store these products in two arrays, then multiply corresponding prefix and suffix values to get the result for each index.
        This approach is straightforward and easy to understand, but uses extra space for the prefix and suffix arrays.
    
    Time Complexity: O(N), where N is the length of nums.
    Space Complexity: O(N) for the prefix and suffix arrays.
    
    Steps:
        1. Initialize prefix and suffix arrays of size N, and an output array.
        2. Compute prefix products: prefix[i] is the product of all elements before index i. (e.g prefix[i] = prefix[i-1] * nums[i-1])
        3. Compute suffix products: suffix[i] is the product of all elements after index i. (e.g suffix[i] = suffix[i+1] * nums[i+1])
        4. For each index, multiply prefix[i] and suffix[i] to get the result.
        5. Return the output array.
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
    Computes the product of the array except itself without using extra space (except for the output array).
    
    Intuition:
        Use the output array to store prefix products in the first pass, then multiply by suffix products in the second pass.
        This avoids using separate prefix/suffix arrays and achieves O(1) extra space (excluding the output).
        
        - First pass: For each index, store the product of all elements to the left (prefix).
        - Second pass: Traverse from right to left, multiplying each index by the product of all elements to the right (suffix).
        - This way, each position contains the product of all elements except itself.
    
    Time Complexity: O(N), where N is the length of nums.
    Space Complexity: O(1) extra space (output array not counted).
    
    Steps:
        1. Initialize the output array with 1s.
        2. Traverse left to right, for each index store the prefix product in the output array.
        3. Traverse right to left, for each index multiply the output by the suffix product.
        4. Return the output array.
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
