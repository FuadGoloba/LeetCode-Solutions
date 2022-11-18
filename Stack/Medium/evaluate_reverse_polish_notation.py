# Evaluate Reverse Polish Notation

# Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
# Note that division between two integers should truncate toward zero. It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


def evalRPN1(tokens):
    '''
        Using a Stack and hashmap; Time = O(n), memory = O(n)
    '''
    
    import operator
    operations = { # Hashmap to map each string operator to its operation
        '+': operator.add,
        '-': operator.sub,
        '*':operator.mul,
        '/':operator.truediv
    }
    # Stack to store operands for immediate operations and pop operands after calculation
    stack = []
    
    # Go through all items in the tokens list
    for item in tokens:
        if item in operations: # If item is an operator, perform operation on the top 2 non operands of the stack and pop the 2 non operands afterwards
            res = int(operations[item](stack[-2], stack[-1]))
            stack.pop()
            stack.pop()
            stack.append(res) # push the result of the current operation to the stack to perform next operation
        else:
            stack.append(int(item)) # if it's an operand, push operand to the top of the stack
            
    return stack[-1] # return the last item in the stack which will be the result of all operations

def evalRPN2(tokens):
    '''
        Using a stack, Time = O(n), Memory = O(1)
    '''
    stack = []
    
    for item in tokens:
        if item == '+':
            stack.append(stack.pop() + stack.pop())
        elif item == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif item == '*':
            stack.append(stack.pop() * stack.pop())
        elif item == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(item))
            
    return stack[-1]
    

if __name__  == '__main__':
    for tokens in [["2","1","+","3","*"], ["4","13","5","/","+"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"], ["0","3","/"]]:
        print(evalRPN2(tokens))
    