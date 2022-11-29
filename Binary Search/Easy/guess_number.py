# Guess Number Higher or Lower

# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.


# Example 1
# Input: n = 10, pick = 6
# Output: 6

# Example 2:
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
# Input: n = 2, pick = 1
# Output: 1

def guessNumber(n):
    
    low, high = 0, n # Initialise 2 pointers for the first version and the lastest version
    
    while low <= high:
        mid = (low + high) // 2
        
        # if our guess is lower than the number picked, then we incease our search range to the higher values
        if guess(mid) == 1:
            low = mid + 1
        
        # If our guess is higher than the number picked, then we reduce our search range to the lower values
        elif guess(mid) == -1:
            high = mid - 1
            
        else:
            return mid
        
        
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    
    # Your guess is lower than the number I picked
    if pick > num:
        return 1
    
    # Your guess is higher than the number I picked
    elif pick < num:
        return -1
    # You guessed the numbe rI picked
    else:
        return 0
    
    
if __name__ == '__main__':
    for n, pick in [(10, 6), (1, 1), (2, 1)]:
        print(guessNumber(n))