""" Generate Parentheses

    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    
    Example 2:
    Input: n = 1
    Output: ["()"]
    
    Constraints:

    1 <= n <= 8
    
"""

def generateParenthesis(n: int) -> list[str]:
    """
        Generates all combinations of well-formed parentheses.
        Using Stack data structure and Backtracking method
    
    Args:
        n (int): number of parentheses pair

    Returns:
        list[str]: combination of well formed parentheses
        
    SOLUTION:
        The intuition is to use backtracking method and a stack to store parentheses and pop
        1. Recursive Exploration: We create a function to build valid strings by making recursive calls which explores all possible sequences of opening and closing parentheses.
        2. Valid Conditions: A valid sequence must always have at least as many open parentheses as closed ones at any point. The recursion only proceeds when these constraints are satisfied.
                             Open parenthesis '(' can be added as long as count of open parentheses < number of pairs (n)
                             Closed parenthesis ) can be added only if if count of closed parentheses < count of open parentheses (to ensure valid order)
        3. Base Case: When open_count == closed_count == n, we have a valid string, so it gets stored in a stack data structure
        4. Backtracking (Undo and explore other options): After adding a parenthesis, the function calls itself recursively to continue building the sequence.
                                                          Once a sequence is fully formed, it is stored in the stack, and the function backtracks by removing the last character from the stack to explore different possibilities.
    """
    
    # Conditions
    # Only add open parenthesis if count of open parentheses < number of pairs (n)
    # Only add closed parenthesis if count of closed parentheses < count of open parentheses
    # Base case - well-formed parentheses is when len(open) == len(closed) == n

    all_combinations = []
    stack = []

    def backtrack(open_count, closed_count):
        # Base case
        if open_count == closed_count == n:
            valid_parentheses = "".join(stack)
            all_combinations.append(valid_parentheses)

        # Condition to add open parenthesis
        if open_count < n:
            stack.append("(")
            backtrack(open_count + 1, closed_count)
            stack.pop()

        # Condition to add closed parenthesis
        if closed_count < open_count:
            stack.append(")")
            backtrack(open_count, closed_count + 1)
            stack.pop()

    backtrack(0, 0)
    return all_combinations

if __name__ == '__main__':
    for n in [1, 2, 3]:
        print(generateParenthesis(n))