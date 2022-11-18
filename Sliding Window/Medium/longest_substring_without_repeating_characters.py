# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    '''
        Using a Sliding Window and Hashset to keep track of duplicate char; Time = O(n), Memory = O(n)
    '''
    seen = set() # Initiliase a hashset to keep track of character's we've come across
    left = 0 # Left pointer to traverse the string (start of a window)
    max_len = 0
    
    # Traversing the string checking a window of a substring with non-repeated characters
    for right in range(len(s)):
        while s[right] in seen: #  check if there's a repeated character in our current window and remove the duplicate character as well as move our left pointer to the next index to start a new window
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, len(seen)) # Update the maxiumum length of substring
        
    return max_len

if __name__ == '__main__':
    for s in ["abcabcbb", "bbbbb", "pwwkew"]:
        print(lengthOfLongestSubstring(s))