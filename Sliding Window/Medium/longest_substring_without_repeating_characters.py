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
        Returns the length of the longest substring without repeating characters in a given string s. Using a Sliding Window and Hashset to keep track of duplicate characters.

        Intuition:
            we can keep one window that always has unique characters. We expand the window by moving the right pointer.
            If we ever see a repeated character, we shrink the window from the left until the duplicate is removed.
            This way, the window always represents a valid substring, and we track its maximum size.
            It's efficient because each character is added and removed at most once.
            
        Steps:
            1. Initialize a hashset and two pointers (left, right).
            2. Move right pointer, adding unique characters to the set.
            3. If a duplicate is found, remove characters from the set by moving left pointer.
            4. Track and update the maximum window size.
            5. Return the maximum length found.
            
        Time Complexity: O(n) - Each character is visited at most twice (once by right pointer and once by left pointer).
        Space Complexity: O(n) - In the worst case, the hashset can contain all unique characters in the string.
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
        Returns the length of the longest substring without repeating characters in a given string s. Using a Sliding Window and Hashset to keep track of duplicate characters
        
        Intuition:
            we can keep one window that always has unique characters. We expand the window by moving the right pointer.
            If we ever see a repeated character, we shrink the window from the left until the duplicate is removed.
            This way, the window always represents a valid substring, and we track its maximum size.
            It's efficient because each character is added and removed at most once.
            
        Steps:
            1. Initialize a hashset and two pointers (st_wdw, end_wdw).
            2. Move end_wdw pointer, adding unique characters to the set.
            3. If a duplicate is found, remove characters from the set by moving st_wdw pointer.
            4. Track and update the maximum window size.
            5. Return the maximum length found. 
            
        Time Complexity: O(n) - Each character is visited at most twice (once by end_wdw pointer and once by st_wdw pointer).
        Space Complexity: O(n) - In the worst case, the hashset can contain all unique characters in the string.
    """
    st_wdw, end_wdw, max_len = 0, 0, 0
    window = set()

    while end_wdw < len(s):
        if s[end_wdw] in window:
            window.remove(s[st_wdw])
            st_wdw += 1
        else:
            window.add(s[end_wdw])
            max_len = max(max_len, (end_wdw - st_wdw) + 1)
            end_wdw += 1
    return max_len

def lengthOfLongestSubstring3(s: str) -> int:
    """
        Returns the length of the longest substring without repeating characters in a given string s. Using a Sliding Window and Hashmap to keep track of duplicate characters and their counts.
        
        Intuition:
            The intuition follows similar to using a hashset except that you use a hashmap to store the characters and their counts. 
            Deduct the count when a repeated character is encountered.
            
        Steps:
            1. Initialize a hashmap and two pointers (left, right).
            2. Move right pointer, adding unique characters to the hashmap and their counts.
            3. If a duplicate is found, deduct the count of characters from the hashmap by moving left pointer until the duplicate is removed.
            4. Track and update the maximum window size.
            5. Return the maximum length found.

        Time Complexity: O(n) - Each character is visited at most twice (once by right pointer and once by left pointer).
        Space Complexity: O(n) - In the worst case, the hashmap can contain all unique characters in the string.
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
        Returns the length of the longest substring without repeating characters in a given string s. Using a Sliding Window and an array to keep track of duplicate characters and their counts.

        Intuition:
            The intuition follows similar to using a hashset/hashmap except that you use an array of fixed size to store the character counts. 
            Deduct the count when a repeated character is encountered.
            
        Steps:
            1. Initialize an array of size 128 (assuming ASCII) and two pointers (left, right).
            2. Move right pointer, adding unique characters to the array and their counts.
            3. If a duplicate is found, deduct the count of characters from the array by moving left pointer until the duplicate is removed.
            4. Track and update the maximum window size.
            5. Return the maximum length found. 
            
        Time Complexity: O(n) - Each character is visited at most twice (once by right pointer and once by left pointer).
        Space Complexity: O(1) - The array size is fixed (128 for ASCII), regardless of the input string size.
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