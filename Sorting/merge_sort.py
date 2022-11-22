# The Merge Sort algorithm is a sorting algorithm that is based on the Divide and Conquer paradigm. In this algorithm, the array is initially divided into two equal halves and then they are combined in a sorted manner.

# Think of it as a recursive algorithm continuously splits the array in half until it cannot be further divided. 
# This means that if the array becomes empty or has only one element left, the dividing will stop, i.e. it is the base case to stop the recursion. 
# If the array has multiple elements, split the array into halves and recursively invoke the merge sort on each of the halves. 
# Finally, when both halves are sorted, the merge operation is applied. Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.

# Running time - O(nlogn); merging Two sorted array- O(n); recursion and splitting - O(logn)
# Memory - O(n)

def merge_sort(arr):

    # Base case; 

    if len(arr) == 1:
        return arr

    # Split array into halves
    mid = len(arr) // 2

    # Recursively merge-sort both halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge both sorted halves of the array
    result = merge2(left, right)

    return result


# Merging Two sorted arrays
def merge(left, right):

    # result of combined array
    res = []

    # Lopp through till both arrays are empty
    while left and right:
        i = left[0] # first element of left array
        j = right[0] # first element of right array

        # get the min of both sorted arrays and move to the result list;
        if i < j:
            res.append(i)
            left.remove(i)
        else:
            res.append(j)
            right.remove(j)

    # Include whatever's remaining from either array to the result array
    res.extend(left)
    res.extend(right)
    # Return result list
    return res

def merge2(left, right):

    res = [0] * (len(left) + len(right)) # A result array the size of both left and right arrays
    l = r = 0 # l and r represent index pointers for left and right arrays respectively
    res_idx = 0 # index position in the result array

    # Loop through till we get to the end of both arrays
    while l < len(left) and r < len(right):

        # Compare first element of both arrays and add the smallest to the result array
        if left[l] < right[r]:
            res[res_idx] = left[l]
            l += 1 # point index pointer to next index
        else:
            res[res_idx] = right[r]
            r += 1
        res_idx += 1 # point index pointer of result array to nect index

    # Add remainder of whatever's left from either of the arrays to the resulting list
    while l < len(left):
        res[res_idx] = left[l]
        l += 1
        res_idx += 1

    while r < len(right):
        res[res_idx] = right[r]
        r += 1
        res_idx += 1

    return res

if __name__ == '__main__':

    input_n = int(input('Enter size of array:' ))
    input_arr = list(map(int, input('Enter elements of the array with a space between each :' ).split()))
    assert len(input_arr) == input_n
    print(merge_sort(input_arr))
