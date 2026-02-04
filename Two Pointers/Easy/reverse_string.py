"""
    Write a function that reverses a string. The input string is given as an array of characters s.
    You must do this by modifying the input array in-place with O(1) extra memory.

    Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    
    Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
    
    Constraints:
    1 <= s.length <= 105
    s[i] is a printable ascii character.
"""

def reverse_string(s):
    """
    Reverses a string using the two pointers method.

    Intuition:
        - Use two pointers starting from both ends of the string.
        - Swap characters at each pointer and move towards the center.

    Steps:
        1. Initialize left and right pointers at the start and end of the string.
        2. While left < right:
            - Swap characters at left and right pointers.
            - Move both pointers inward.
        3. Return the reversed string.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1), constant extra space.
    """
    left_idx, right_idx = 0, len(s) - 1
    while left_idx < right_idx:
        s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
        left_idx += 1
        right_idx -= 1
    return s
def reverse_string_2(s):
    """
    Reverses a string using the two pointers method.

    Intuition:
        - Use two pointers starting from both ends of the string.
        - Swap characters at each pointer and move towards the center.

    Steps:
        1. Initialize left and right pointers at the start and end of the string.
        2. While left < right:
            - Swap characters at left and right pointers.
            - Move both pointers inward.
        3. Return the reversed string.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1), constant extra space.
        """
    left_pointer = 0
    right_pointer = len(s) - 1
    s = list(s)  # Convert string to list for mutability
    while left_pointer < right_pointer:
        s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
        left_pointer += 1
        right_pointer -= 1
    return ''.join(s)

def reverse_string_3(s):
    """
    Reverses a string using an auxiliary array.
    
    Intuition:
        - Create a temporary array to store characters in reverse order.
        - Copy characters from the temporary array back to the original array.
    Steps:
        1. Create a temporary array.
        2. Fill the temporary array with characters from the original array in reverse order.
        3. Copy characters from the temporary array back to the original array.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), for the temporary array.
    """
    tmp = []
    for i in range(len(s) - 1, -1, -1):
        tmp.append(s[i])
    for i in range(len(s)):
        s[i] = tmp[i]

def reverse_string_4(s):
    """
    Reverses a string using a stack.
    
    Intuition:
        - Use a stack to store characters and then pop them to reverse the string.
    Steps:
        1. Push all characters onto a stack.
        2. Pop characters from the stack and overwrite the original string.
        
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), for the stack.
    """     
    stack = []
    for c in s:
        stack.append(c)
    i = 0
    while stack:
        s[i] = stack.pop()
        i += 1

def reverse_string_5(s):
    """
    Reverses a string using Python's slicing method.

    Intuition:
        - Python allows easy reversal of strings using slicing.

    Steps:
        1. Use slicing to reverse the string.
        2. Return the reversed string.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), for the new reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    test_cases = [
        ["h","e","l","l","o"],
        ["H","a","n","n","a","h"],
        ["A","B","C","D","E","F"],
        ["1","2","3","4","5"]
    ]
    
    for case in test_cases:
        reversed_case = reverse_string(case.copy())
        print(f"Original: {case}\nReversed: {reversed_case}\n") 