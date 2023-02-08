# Top K Frequent Elements
#   Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


def topKFrequent1(nums, k):
    '''
        Using a hashmap to map numbers to their frequencies and sorting based on frequencey to get the most frequent; Time = O(nlogn), Memory = O(n)
    '''
    result = []
    
    counter_dict = {}
    for num in nums:
        counter_dict[num] = counter_dict.get(num, 0) + 1

    sorted_freq = sorted(counter_dict.items(), reverse=True, key=lambda kv:kv[1])
    
    for num, freq in sorted_freq:
        if len(result) < k:
            result.append(num)
            
    return result


def topKFrequent2(nums, k):
    '''
        Using hashmap and Buckect sort; Time = O(n), Memory = O(n)
    '''
    frequencyMap = {} # Hashmap to map items to their frequency
    freq_list = [[] for i in range(len(nums) + 1)] # List to store a list for every index of the array
    
    # Traverse the array mapping each item to its frequency
    for item in nums:
        frequencyMap[item] = frequencyMap.get(item, 0) + 1
    
    # Traverse the frequency map and for each index/count in the frequency list(index <=> count), append the item to the list (So you have a list of list of hashmap's keys where the index is the count/frequency of the key)
    for item, count in frequencyMap.items():
        freq_list[count].append(item)
    
    result = [] # Result to store top K frequent elements
    # Traverse the list starting from the end, each item to the 1th index
    for index in range(len(freq_list) - 1, 0, -1): 
        for item in freq_list[index]: # Traverse the inner list of each index (i.e each index here is the count/frequency) and append the numbers in the list to the final result list
            result.append(item)
            if len(result) == k:
                return result

if __name__ == '__main__':
    for arr, k in [([1,1,1,2,2,3],2), ([1],1), ([1,2],2)]:
        print(topKFrequent2(arr, k))
                
    