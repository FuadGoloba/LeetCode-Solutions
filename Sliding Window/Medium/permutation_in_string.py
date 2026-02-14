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
        Returns true if s2 contains a permutation of s1, or false otherwise. Uses Sliding Window and hashmaps.

        Intuition:
        The goal is to check if any substring of s2 with length equal to s1 is a permutation of s1.
        To do this efficiently, we use a sliding window of size len(s1) over s2 and maintain frequency counters (hashmaps) for both s1 and the current window in s2.

        - First, we build a frequency counter for s1, counting how many times each character appears.
        - We also build a frequency counter for the first window in s2 (the first len(s1) characters).
        - As we slide the window through s2, we update the s2 counter:
            - Remove the count of the character that is sliding out of the window (the leftmost character).
            - Add the count of the new character entering the window (the rightmost character).
        - At each step, we compare the two counters:
            - If they match, it means the current window in s2 is a permutation of s1, so we return True.
        - If no window matches after sliding through s2, we return False.

        This approach ensures we only update the counters incrementally, making it efficient.
        
        Steps:
        1. Check if s1 is longer than s2. If it is, return False immediately, since s2 cannot contain a permutation of s1.
        2. Initialize two frequency counters (hashmaps) for s1 and the initial window in s2.
        3. Slide the window across s2, updating the counters and checking for matches at each step.
        4. After the loop, perform a final check for the last window in s2.
        5. Return True if a match is found, otherwise return False.
        
    Time Complexity: O(n) where n is the length of s2, since we are sliding through s2 once.
    Space Complexity: O(k) where k is the number of unique characters in s1, since we are storing the frequency counts in hashmaps.
        
    '''
    if len(s1) > len(s2):
        return False

    s1_counter, s2_counter = {}, {}
    
    # Build frequency counters for s1 and the initial window in s2
    for i in range(len(s1)):
        s1_counter[s1[i]] = s1_counter.get(s1[i], 0) + 1
        s2_counter[s2[i]] = s2_counter.get(s2[i], 0) + 1

    # Slide the window across s2
    for r in range(len(s1), len(s2)):
        if s1_counter == s2_counter:
            return True

        # Remove the leftmost character from the window
        left_char = s2[r - len(s1)]
        if s2_counter[left_char] == 1:
            s2_counter.pop(left_char)
        else:
            s2_counter[left_char] -= 1

        # Add the new rightmost character to the window
        right_char = s2[r]
        s2_counter[right_char] = s2_counter.get(right_char, 0) + 1

    # Final check for the last window
    return s1_counter == s2_counter


def checkInclusion3(s1: str, s2: str) -> bool:
    '''
        Returns true if s2 contains a permutation of s1, or false otherwise. Uses Sliding Window and frequency counters in the form of arrays.        
        
        Intuition:
        Similar to the previous solution, we want to check if any substring of s2 with length equal to s1 is a permutation of s1. 
        Instead of using hashmaps for frequency counting, we can use fixed-size arrays since we are only dealing with lowercase English letters (26 characters).
        
        - We create two frequency counters as arrays of size 26, where each index corresponds to a character ('a' to 'z').
        - We populate the frequency counters for s1 and the initial window in s2.
        - As we slide the window through s2, we update the frequency counters by incrementing the count for the new character and decrementing the count for the character that is sliding out of the window.
        - We compare the two frequency counters at each step to check for a match.    
        
        This approach is more space-efficient than using hashmaps, as the size of the frequency counters is fixed at 26, regardless of the input size.  
        
        Steps:
        1. Check if s1 is longer than s2. If it is, return False immediately, since s2 cannot contain a permutation of s1.
        2. Initialize two frequency counters as arrays of size 26 for s1 and the initial window in s2.
        3. Slide the window across s2, updating the frequency counters and checking for matches at each step.
        4. After the loop, perform a final check for the last window in s2.
        5. Return True if a match is found, otherwise return False. 
        
    Time Complexity: O(n) where n is the length of s2, since we are sliding through s2 once.
    Space Complexity: O(1) since the frequency counters are fixed-size arrays of length 26, regardless of the input size.   
    '''
    # Step 1: If s1 is longer than s2, s2 cannot contain a permutation of s1
    if len(s1) > len(s2):
        return False

    # Step 2: Initialize frequency counters as arrays of size 26 for s1 and the initial window in s2
    s1_counter, s2_counter = [0] * 26, [0] * 26
    
    # Step 3: Populate the frequency counters for s1 and the initial window in s2
    for i in range(len(s1)):
        s1_counter[ord(s1[i]) - ord('a')] += 1
        s2_counter[ord(s2[i]) - ord('a')] += 1

    # Step 4: Slide the window across s2, updating counters and checking for matches
    for r in range(len(s1), len(s2)):
        if s1_counter == s2_counter:
            return True
        
        # Remove the count for the character sliding out of the window
        s2_counter[ord(s2[r - len(s1)]) - ord('a')] -= 1
        # Add the count for the new character entering the window
        s2_counter[ord(s2[r]) - ord('a')] += 1

    # Step 5: Final check for the last window
    return s1_counter == s2_counter


if __name__ == '__main__':
    for s1, s2 in [("ab", "eidbaooo"), ("ab", "eidboaoo"), ("a", "ab")]:
        print(check_inclusion(s1, s2)) # True, False, True
        assert check_inclusion(s1, s2) == checkInclusion2(s1, s2) == checkInclusion3(s1, s2)