# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
            # Open brackets must be closed by the same type of brackets.
            # Open brackets must be closed in the correct order.
            # Every close bracket has a corresponding open bracket of the same type.
            
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false


def isValid(s):
    '''
        Using a stack data structure and hashmap for lookup; Time = O(n), Memory = O(n)
    '''
    stack = [] # Stack datastructure to store open parenthese
    CloseToOpenMap = {")":"(", "]":"[", "}":"{"} # Dictionary to map every closing parentheses to a corresponding opening parenthese
    # Push every open parenthesis to the stack and check that the element at the top of the stack matches the closing parenthesis; then pop the element from the stack 
    for char in s: # Traverse the string and check that the character is a closing parenthese
        if char in CloseToOpenMap: # Then we check if it's corresponding opening parenthese is at the top of the stack
            if stack and stack[-1] == CloseToOpenMap[char]: # If it's in the stack , then we pop the opehing parenthese fromn the stack as it's follows a valid input
                stack.pop()
            else: # If it's corresponding opening parenthese is not at the top of the stack, then it is an invalid string as every open brackedt must be closed by it's type of bracket in the correct order.
                return False
        else: # If it's not a closing parenthese, we push to the top of the stack
            stack.append(char)
    # If the stack is empty, then we know we have matched every closing parenthesis to its corresponding opening parenthesis
    return True if not stack else False

if __name__ == '__main__':
    for s in ["()", "()[]{}", "(]"]:
        print(isValid(s))
            