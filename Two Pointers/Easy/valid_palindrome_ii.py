"""
    You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.
    A palindrome is a string that reads the same forward and backward.
    Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

    Example 1:
    Input: s = "aca"
    Output: true
    Explanation: "aca" is already a palindrome.

    Example 2:
    Input: s = "abbadc"
    Output: false
    Explanation: "abbadc" is not a palindrome and can't be made a palindrome after deleting at most one character.

    Example 3:
    Input: s = "abbda"
    Output: true
    Explanation: "We can delete the character 'd'.

    Constraints:
    1 <= s.length <= 100,000
    s is made up of only lowercase English letters. 

"""

def valid_palindrome(s):
    """
    Checks if a string can be a palindrome after deleting at most one character.

    Intuition:
        - Use two pointers to compare characters from both ends.
        - If a mismatch is found, check the two possible substrings formed by deleting one character.

    Steps:
        1. Initialize left and right pointers.
        2. While left < right:
            - If characters at left and right are equal, move both pointers inward.
            - If not equal, check the two possible substrings:
                - One by deleting the character at the left pointer.
                - Another by deleting the character at the right pointer.
        3. If no mismatches are found, the string is a palindrome.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), for the temporary substrings.
    """
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            del_left = s[left + 1 : right + 1] # delete left end from string
            del_right = s[left : right] # delete right end from string

            return (del_left == del_left[::-1] or del_right == del_right[::-1]) # check if they are palindromic after deletion form either end

        left, right = left + 1, right - 1
        return True
    
def valid_palindrome_optimal(s):
    """
    Checks if a string can be a palindrome after deleting at most one character.
    Intuition:
        - Use two pointers to compare characters from both ends.
        - If a mismatch is found, check the two possible substrings formed by deleting one character.
        
    Steps:
        1. Define a helper function to check if a substring is a palindrome.
        2. Initialize left and right pointers.
        3. While left < right:
            - If characters at left and right are equal, move both pointers inward.
            - If not equal, check the two possible substrings:
                - One by deleting the character at the left pointer.
                - Another by deleting the character at the right pointer.
        4. If no mismatches are found, the string is a palindrome.
        
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1), for the helper function's space usage.
    """

    def is_palindrome_range(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        
        left, right = left + 1, right - 1
        return True
    
if __name__ == "__main__":
    test_cases = [
        "aba",
        "abca",
        "abc",
        "deeee",
        "eeeed"
    ]

    for case in test_cases:
        print(f"Input: {case} -> Output: {valid_palindrome_optimal(case)}")