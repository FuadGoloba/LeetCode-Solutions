"""Longest Substring Without Repeating Characters

    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    
    Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
    '''
        Using a Sliding Window and Hashset to keep track of duplicate char; Time = O(n), Memory = O(n)
        
        SOLUTION:
            The intuition is to use a sliding window technique and a hashset. We create a window using two pointers (l and r) and adding characters to the hashset and computing the length of the unique substring added. (l for marking the start of a window and r for traversing the string)
            When we encounter a character that's already in the hashset, we shrink the window, removing the characters from the hashset and adjusting the left pointer till we start a new window (i.e hashset is empty for the new window).
    '''
    seen = set() # Initiliase a hashset to keep track of character's we've come across
    left = 0 # Left pointer (start of a window)
    max_len = 0
    
    # Traversing the string with the right pointer checking a window of a substring with non-repeated characters
    for right in range(len(s)):
        while s[right] in seen: #  check if there's a repeated character in our current window and remove all characters from the set while moving our left pointer till the start of a new window
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, (right - left) + 1) # Update the maxiumum length of substring
        
    return max_len

def lengthOfLongestSubstring2(s: str) -> int:
    """
        Using a Sliding Window and Hashset to keep track of duplicate char; Time = O(n), Memory = O(n)
        
        SOLUTION:
            The intuition is to use a sliding window technique and a hashset. We create a window using two pointers (l and r) and adding characters to the hashset and computing the length of the unique substring added. (l for marking the start of a window and r for traversing the string)
            When we encounter a character that's already in the hashset, we shrink the window, removing the characters from the hashset and adjusting the left pointer till we start a new window (i.e hashset is empty for the new window).
    """
    max_length = 0
    l, r = 0, 0
    hashset = set()

    while r < len(s):
        if s[r] not in hashset:
            hashset.add(s[r])
            max_length = max(max_length, (r-l) + 1)
            r += 1 # Only move to the next character if we haven't repeated characters in a window
        else:
            # Keep removing characters from the hashset and adjusting the left pointer till all elements are removed and we can start a new window 
            hashset.remove(s[l])
            l += 1
    return max_length

def lengthOfLongestSubstring3(s: str) -> int:
    """
        Using a Sliding Window and a hashmap to keep track of duplicates characters and their count; Time = O(n), Memory = o(n)
        
        SOLUTION:
            The intuition follows similar to using a hashset except that you use a hashmap to store the characters and their counts. Deduct the count when a repeated character is encountered.
    """
    
    map = {}
    max_len = 0
    left = 0
    
    for right, char in enumerate(s):
        map[char] = map.get(char, 0) + 1 # similar to hashset.add()
        while map[char] > 1:
            map[s[left]] -= 1 # similar to hashset.remove()
            left += 1
        max_len = max(max_len, (right - left) + 1)

    return max_len

def lengthOfLongestSubstring4(s: str) -> int:
    """
        Using a Sliding Window and a fixed array with size (128) of all english letters, digits, symbols and spaces; to keep track of character count whereby the ascii number of the character represents the index.
        ; Time = O(n), Memory = o(n) ; Most efficient method
        
        SOLUTION:
            The intuition follows similar to using a hashset/hashmap except that you use an array of fixed size to store the character counts. Deduct the count when a repeated character is encountered.
    """
    max_len = 0
    left = 0
    char_arr = [0] * 128
    
    for right in range(len(s)):
        char = ord(s[right])
        while char_arr[char] > 0:
            char_arr[ord(s[left])] -= 1
            left += 1
        char_arr[char] += 1
        max_len = max(max_len, (right - left) + 1)

    return max_len
        
if __name__ == '__main__':
    for s in ["abcabcbb", "bbbbb", "pwwkew"]:
        print(lengthOfLongestSubstring(s))
        assert(lengthOfLongestSubstring(s) == lengthOfLongestSubstring2(s) == lengthOfLongestSubstring3(s) == lengthOfLongestSubstring4(s))