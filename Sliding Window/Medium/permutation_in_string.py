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

if __name__ == '__main__':
    for s1, s2 in [("ab", "eidbaooo"), ("ab", "eidboaoo"), ("a", "ab")]:
        print(check_inclusion(s1, s2))