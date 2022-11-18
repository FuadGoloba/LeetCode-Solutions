# Valid Anagram {EASY}

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#   An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


def isAnagram1(s, t):
    '''
        Sorting both strings; Time = O(nlogn), memory = O(1)
    '''
    return str(sorted(s)) == str(sorted(t))

def isAnagram2(s, t):
    '''
        Using an Array to store count of characters; Time = O(n), Memory = O(n)
    '''
    if len(s) != len(t):
        return False
    
     # create an array of length 26 to store count of characters in each word
    char_count_s = [0] * 26
    char_count_t = [0] * 26
    
    # Loop through characters in each word
    for idx in range(len(s)):
        # increment the count of the character for both s and t
        char_count_s[ord(s[idx]) - ord('a')] += 1
        char_count_t[ord(t[idx]) - ord('a')] += 1
        
    return char_count_s == char_count_t


def isAnagram3(s, t):
    '''
        Using a hashmap to store count of characters; Time = O(n), Memory = O(n)
    '''
    if len(s) != len(t):
        return False
    
    # Hashmap to map each word to its count
    counterS, counterT = {}, {}
    
    # Traverse the words and get their count
    for i in range(len(s)):
        counterS[s[i]] = counterS.get(s[i], 0) + 1
        counterT[t[i]] = counterT.get(t[i], 0) + 1
    # return true if both hashmaps contain same elements
    return counterS == counterT
    
    

if __name__ == '__main__':
    for s, t in [("anagram", "nagaram"), ("rat","car")]:
        print(isAnagram2(s, t))
    