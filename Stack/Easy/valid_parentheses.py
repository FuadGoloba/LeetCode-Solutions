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
    """
        Return True if the string of parentheses is valid, otherwise False.
        
        Intuition:
        We can use a stack to keep track of the most recent opening bracket and match it with the closing bracket as we traverse the string.
        This ensures that we only close brackets in the correct order. So we enter an opening bracket, we push the corresponding closing bracket onto the stack. 
        When we encounter a closing bracket, we check if it matches the top of the stack. If it does, we pop it from the stack; otherwise, it's invalid.

        Steps:
        1. Create a mapping of opening brackets to their corresponding closing brackets.
        2. Initialize an empty stack to keep track of opening brackets.
        3. Traverse each character in the string:
            - If it's an opening bracket, push the corresponding closing bracket onto the stack.
            - If it's a closing bracket, check if the stack is empty or if the top of the stack does not match the closing bracket. If either condition is true, return False.
        4. After traversing the string, check if the stack is empty. If it is empty, return True; otherwise, return False.  
        
        Time Complexity: O(n) where n is the length of the string, as we traverse the string once.
        Space Complexity: O(n) in the worst case when all characters are opening brackets, as we would push all of them onto the stack.
    """
    openToClose = {'(':')', '[':']', '{': '}'}
    stack = []

    for p in s:
        if p in openToClose: # If it's an opening bracket, we push the corresponding closing bracket onto the stack
            stack.append(openToClose[p])
        else: # If it's a closing bracket, we check if the stack is empty or if the top of the stack does not match the closing bracket. If either condition is true, return False.
            if not stack or stack.pop() != p:
                return False
    return True if not stack else False

def isValid2(s: str) -> bool:
    '''
        Returns true if the string of parentheses is valid, otherwise false.
        
        Intuition:
            The intuition is to use a stack data structure as it supports LIFO to match closing brackets to the most recent opening bracket (i.e element at the top of the stack),
            Open parentheses are pushed to the top of the stack and popped against an immediate matching closing bracket if encountered
        
        Steps:
        1: Create a hashmap to map closing brackets to their corresponding opening brackets
        2: Traverse each parenthesis and if open bracket, push to the top of the stack. If closing bracket, the stack must not be empty; check that element at the top of the stack is a matching open bracket and pop it, otherwise return False because there's a mismatch
            This means that, every recent closing bracket we come across must have a corresponding matching open bracket at the top of the stack. (Stack must not be empty) so we pop it from the top of the stack if it matches so we can check the next match otherwise there's a mismatch and we return false

        3: At the end of the string traversal, we check that the stack is empty as an empty stack means we found all matching pairs. If not empty, then for sure, it's not a valid string with the correct order of bracket pair
        4. Return True if the stack is empty, otherwise False.
        
        Time Complexity: O(n) where n is the length of the string, as we traverse the string once.
        Space Complexity: O(n) in the worst case when all characters are opening brackets, as we would push all of them onto the stack.
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
        print(isValid(s)) # True, True, False, True, False
        print(isValid2(s)) # True, True, False, True, False
        assert isValid(s) == isValid2(s)
