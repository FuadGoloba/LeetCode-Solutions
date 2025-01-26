"""
    Permutation in String
    
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
    In other words, return true if one of s1's permutations is the substring of s2.
    
    Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
    
    Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false
    
    Constraints:
    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
"""

def check_inclusion(s1: str, s2: str) -> bool:
    """
        Using sliding window and hashmaps, Time = O(n), Memory = O(k) where k is the number of unique characters in s1
    
        Args:
            s1 (str): string
            s2 (str): string

        Returns:
            bool: any of s1's permutations is a substring of s2
            
        SOLUTION:
            The intuition is to use a sliding window with a frequency counter. 
            Step 1: Use a frequency counter (hashmap) to store the character count of s1
            Step 2: Create a counter for s2 and maintain a sliding window of size len(s1) to go over s2 characters and add to s2 counter
            Step 3: Adjust the window dynamically by adding new character from s2 into s2 counter and removing left most character as the window slides and exceeds the len(s1)
            Step 4: Keep checking if the current s2 counter matches s1 counter
    """
    s1_counter, s2_counter = {}, {}
    l = 0
    
    for char in s1:
        s1_counter[char] = s1_counter.get(char, 0) + 1
        
    for r in range(len(s2)):
        s2_counter[s2[r]] = s2_counter.get(s2[r], 0) + 1

        if (r - l + 1) > len(s1):
            # decrement or remove leftmost character 
            if s2_counter[s2[l]] == 1:
                del s2_counter[s2[l]]
            else:
                s2_counter[s2[l]] -= 1
            
            l += 1
        # check that there's a match between counters of s1 and s2 
        if s1_counter == s2_counter:
            return True
    return False


def checkInclusion2(s1: str, s2: str) -> bool:
    '''
        Using Sliding Window and hashmaps, Time = O(n), Memory = O(k) where k is the number of unique characters in s1
        
        SOLUTION:
            The intuition is to use a sliding window with a frequency counter in the form of a hashmap. And then compare the items in both counters
            Step1: We create two frequency counter, one for s1 and one for s2. We populate s1_counter with all characters of s1 and their freq. We populate s2_counter with window size(i.e. len(s1)) characters of s2.
                   This means that we are creating a len(s1) window_size of characters in s2_counter.
            Step2: We start to traverse the rest of s2 chars from the parts that haven't been entered in  s2counter while removing the frequency count of left most character and entering the next char into the counter; maintaining the window_size (len(s1))
            Step3: At each step of the sliding window, we compare the frequency counts of the current window(s2_counter) and s1_counter. If they match, then that window of s2_counter contains a permutation of s1 and return True     
    '''
    if len(s1) > len(s2):
        return False

    s1_counter, s2_counter = {}, {}
    
    # Create frequency counters for s1 and s2. s2_counter contains characters from s2 the size of the window (i.e len(s1))
    for i in range(len(s1)):
        s1_counter[s1[i]] = s1_counter.get(s1[i], 0) + 1
        s2_counter[s2[i]] = s2_counter.get(s2[i], 0) + 1

    # Slide the window; eliminating the leftmost character from s2_counter and adding a new character to compare the items of teh current window; (i.e if s2counter matches s1_counter)
    for r in range(len(s1), len(s2)):
        if s1_counter == s2_counter:
            return True

        if s2_counter[s2[r - len(s1)]] == 1:
            s2_counter.pop(s2[r - len(s1)])
        else:
            s2_counter[s2[r - len(s1)]] -= 1

        s2_counter[s2[r]] = s2_counter.get(s2[r], 0) + 1

    return s1_counter == s2_counter


def checkInclusion3(s1: str, s2: str) -> bool:
    '''
        Using Sliding Window and arrays, Time = O(n), Memory = O(26)
        
        SOLUTION:
            The intuition is to use a sliding window with a frequency counter in the form of an array the size of the english letters. And then compare the items in both counters
            Step1: We create two frequency counter, one for s1 and one for s2. We populate s1_counter with all characters of s1 and their freq. We populate s2_counter with window size(i.e. len(s1)) characters of s2.
                   This means that we are creating a len(s1) window_size of characters in s2_counter.
            Step2: We start to traverse the rest of s2 chars from the parts that haven't been entered in  s2counter while removing the frequency count of left most character and entering the next char into the counter; maintaining the window_size (len(s1))
            Step3: At each step of the sliding window, we compare the frequency counts of the current window(s2_counter) and s1_counter. If they match, then that window of s2_counter contains a permutation of s1 and return True     
    '''
    if len(s1) > len(s2):
        return False

    s1_counter, s2_counter = [0] * 26, [0] * 26
    
    for i in range(len(s1)):
        s1_counter[ord(s1[i]) - ord('a')] += 1
        s2_counter[ord(s2[i]) - ord('a')] += 1

    for r in range(len(s1), len(s2)):
        if s1_counter == s2_counter:
            return True
        
        s2_counter[ord(s2[r - len(s1)]) - ord('a')] -= 1
        s2_counter[ord(s2[r]) - ord('a')] += 1

    return s1_counter == s2_counter


if __name__ == '__main__':
    for s1, s2 in [("ab", "eidbaooo"), ("ab", "eidboaoo"), ("a", "ab")]:
        print(check_inclusion(s1, s2))
        assert check_inclusion(s1, s2) == checkInclusion2(s1, s2) == checkInclusion3(s1, s2)