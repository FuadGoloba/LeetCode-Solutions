# First Bad Version {EASY}

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


# Example 1:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version

# Example 2:
# Input: n = 1, bad = 1
# Output: 1



def firstBadVersion1(n):
    '''
        Naive Method - Time: O(n), Memory = O(1)
    '''
    # Traverse all versions from the very first version until we encounter the first  bad version and we return
    for version in range(n + 1):
        if isBadVersion(version):
            return version


def firstBadVersion2(n):
    '''
        Efficient Method Using Binary Search; Time = O(logn), Memory = O(1)
    '''
    
    low, high = 0, n # Initialise 2 pointers for the first version and the lastest version
    
    # Traverse all versions until we shrink the search space such that the low = high
    while low != high:
        mid = (low + high) // 2 # divide the search space into 2; 
        
        # if the mid is not a bad version then we move our search space to everything after the mid
        if not isBadVersion(mid):
            low = mid + 1
        
        # If the mid is a bad version, then the first bad version would appear somewhere up till the mid
        else:
            high = mid
            
    return low


# API that returns whether a version is bad (comes with the question)
def isBadVersion(version):
    return version == bad



if __name__ == '__main__':
     for n, bad in [(5, 4), (1, 1)]:
         print(firstBadVersion2(n))