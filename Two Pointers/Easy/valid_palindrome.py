# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#   Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
#   Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.


def is_palindrome1(s):
    '''
        Reversing the string method
    '''
    new_s = "" # Create a new string to store only alphanumeric characters of the input
    
    for char in s:
        if isAlphaNum(char):
            new_s+= char.lower() # Only add alphanumeric characters 
    return new_s == new_s[::-1] # Check that the string and it's reverse are the same
    

def is_palindrome2(s):
    '''
        Using Two pointers; Time = O(n), Memory = O(1)
    '''
    left_pointer = 0 # Initialising a left pointer
    right_pointer = len(s) - 1 #Initialising a right pointer
    
    while (left_pointer < right_pointer): # Ensure that while comparing the left and right pointers, the left and right don't exceed one another
        while left_pointer < right_pointer and not is_alphanum(s[left_pointer]): # we want to skip to the next lkeft pointer if the left pointer contains non alphanumeric characters
            left_pointer += 1
            
        while right_pointer > left_pointer and not is_alphanum(s[right_pointer]): # we want to skip to the next right pointer if the right pointer contains non alphanumeric characters
            right_pointer -= 1
            
        if s[left_pointer].lower() != s[right_pointer].lower(): # Check if the left and right pointer characters are palindromic
            return False
        else:
            left_pointer += 1
            right_pointer -= 1
    return True
            

def isAlphaNum(char):
    return (ord('a') <= ord(char) <= ord('z') or
            ord('A') <= ord(char) <= ord('Z') or 
            ord('0') <= ord(char) <= ord('9'))
    
    
if __name__ == '__main__':
    for s in [ "race a car", "A man, a plan, a canal: Panama", " "]:
        print(is_palindrome2(s))
    
    