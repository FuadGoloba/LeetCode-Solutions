'''
    Valid Parentheses

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
                Open brackets must be closed by the same type of brackets.
                Open brackets must be closed in the correct order.
                Every close bracket has a corresponding open bracket of the same type.
                
    Example 1:
    Input: s = "()"
    Output: true

    Example 2:
    Input: s = "()[]{}"
    Output: true

    Example 3:
    Input: s = "(]"
    Output: false
    
    Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
'''

def isValid(s: str) -> bool:
    '''
        Using a stack data structure, Time = O(n), Memory = O(n)
        
        SOLUTION:
            The intuition is to use a stack data struucture as it supports LIFO to match closing brackets to the most recent opening bracket (i.e element at the top of the stack),
            Open parentheses are pushed to the top of the stack and popped against an immediate matching closing bracket if encountered
            Step 1: Create a hashmap to map closing brackets to their corresponding opening brackets
            Step 2: Traverse each parenthesis and if open bracket, push to the top of the stack. If closing bracket, the stack must not be empty; check that element at the top of the stack is a matching open bracket and pop it, otherwise return False because there's a mismatch
                    This means that, every recent closing bracket we come across must have a corresponding matching open bracket at the top of the stack. (Stack must not be empty) so we pop it from the top of the stack if it matches so we can check the next match otherwise there's a mismatch and we return false
    
            Step 3: At the end of the string traversal, we check that the stack is empty as an empty stack means we found all matching pairs. If not empty, then for sure, it's not a va;id string with the correct order of bracket pair
    '''
    stack = [] # Stack data structure to store open parentheses
    CloseToOpenMap = {")":"(", "]":"[", "}":"{"}
    # Push every open parenthesis to the stack and check that the element at the top of the stack matches the closing parenthesis; then pop the element from the stack 
    for char in s: 
        if char in CloseToOpenMap: # Then we check if it's corresponding opening parenthese is at the top of the stack
            if stack and stack[-1] == CloseToOpenMap[char]: # If it's in the stack , then we pop the opehing parenthese fromn the stack as it's follows a valid input
                stack.pop()
            else: # If it's corresponding opening parenthese is not at the top of the stack or the stack is empty, then it is an invalid string as every open brackedt must be closed by it's type of bracket in the correct order.
                return False
        else: # we push closing bracket to the top of the stack
            stack.append(char)
    # If the stack is empty, then we know we have matched every closing parenthesis to its corresponding opening parenthesis
    return True if not stack else False
    

if __name__ == '__main__':
    for s in ["()", "()[]{}", "(]", "([])", "]"]:
        print(isValid(s))
            