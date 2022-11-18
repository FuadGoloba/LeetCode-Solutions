# Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

def characterReplacement1(s, k):
    '''
        Using Sliding window approach ; Time = O(n), Memory = O(n)
    '''
    freq_map = {} # dictionary to map every character to it's frequency/count

    max_len = 0 # store longest repeating character
    left = 0 # left pointer to start a window/ substring
    
    for right in range(len(s)):
        # get the count/frequency of the character at the right pointer
        freq_map[s[right]] = freq_map.get(s[right], 0) + 1
        
        # Condition for a valid window to allow at most k number of replacements; (right - left + 1) which is the length of current window
        # Note: the left side of the inequality gives us the no of characters we can replace to get a substring with repeated characters (the current count of less frequent characters). But this number must not exceed our allowable replacement number
        while (right-left + 1) - max(freq_map.values()) > k: # Check that current window is valid enough to substitue/replace with any other char k times
            freq_map[s[left]] -= 1 # if not valid; we decrement the count of that character
            left += 1 # and move the loeft pointer to start a new window (i.e shrink the window size)
        
        # Update the longest repeating character valid for k number of replacements
        max_len = max(max_len, right - left + 1)
    return max_len
    
    
def characterReplacement2(s, k):
    '''
        Using Sliding window approach; Time = O(n), Memory = O(n)
    '''
    freq_map = {} # dictionary to map every character to it's frequency/count

    max_len = 0 # store longest repeating character
    left = 0 # left pointer to start a window/ substring
    max_repeat_letter_count = 0
    
    for right in range(len(s)):
        # get the count/frequency of the character at the right pointer
        freq_map[s[right]] = freq_map.get(s[right], 0) + 1
        max_repeat_letter_count = max(max_repeat_letter_count, freq_map[s[right]]) # We get the count of the maximum repeating letter in any window 
        
        # Current window size is from window_start to window_end, overall we have a letter which is repeating 'max_repeat_letter_count' times, this means we can have a window
        # which has one letter repeating 'max_repeat_letter_count' times and the remaining letters we should replace. If the remaining letters are more than 'k', we shrink the window as we are not allowed to replace more than k letters
        if (right - left + 1) - max_repeat_letter_count > k:
            freq_map[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
    
    

if __name__ == '__main__':
    for s, k in [("ABAB", 2), ("AABABBA", 1)]:
        print(characterReplacement2(s, k))