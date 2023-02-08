# Group Anagrams {MEDIUM}

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#   An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

def groupAnagrams1(strs):
    '''
        Using a hashmap; Time = O(m. nlogn), Memory - O(n)
    '''
    dictionary = {}
    
    for word in strs:
        sortedLetters = ''.join(sorted(word))
        dictionary[sortedLetters] = dictionary.setdefault(sortedLetters, []) + [word]
    
    return dictionary.values()


def groupAnagrams2(strs):
    '''
        Using a hashmap without sorting the input string, Time = O(m.n) where m is average number of characters in each word; Memory - O(n)
    '''
    # Dictionary to map group of words with similar characters
    result = {}
    # Loop through words in the array
    for word in strs:
        # create an array of length 26 to store count of characters in each word
        char_count = [0] * 26
        # Loop through characters in each word
        for char in word:
            # increment the count of the character
            char_count[ord(char) - ord('a')] += 1 # ord converts the character to it's integer equivalent; and the difference from ord('a') gives the index of the character
        # Map each word's character count to its word
        result[tuple(char_count)] = result.setdefault(tuple(char_count), []) + [word]
        
    return result.values()
             
        

if __name__ == '__main__':
    for input_strs in [["eat","tea","tan","ate","nat","bat"], [""], ["a"]]:
        print(groupAnagrams2(input_strs))