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
        max_len = max(max_len, len(seen)) # Update the maxiumum length of substring
        
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

if __name__ == '__main__':
    for s in ["abcabcbb", "bbbbb", "pwwkew"]:
        print(lengthOfLongestSubstring(s))