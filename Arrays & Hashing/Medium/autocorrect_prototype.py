# Autocorrect Prototype [ From Coding challenge with Murex]

# Given a list of correct words, and a list of misspelt words, return anagrams of the correct words from their mispelt 

# Example
# Input:
    # words = ["emits", "items", "baker", "times", "break", "cart"]
    # queries = ["mites", "brake"]
# Output : [['emits', 'items', 'times'], ['break', 'baker']]

def autoCorrect(words, queries):
    
    # using a Hashmap and sorting
    
    result = [] # result array to store anagrams
    # loop through the array of words to autocorrect
    for word in queries:
        d = {} # Create a hashmap for each word to autocorrect, mapping the word to an array of its anagrams
        sorted_queries = ''.join(sorted(word))
        d[sorted_queries] = []
        
        # Loop through the array of correct words and add them to their array of anagrams 
        for w in words:
            if ''.join(sorted(w)) in d:
                d[sorted_queries] += [w]
        
        result.append(d.values())
        
    return result


# Solution 2 - Using a hashmap without sorting each word
def autoCorrect2(words, queries):
    result = [] # result array to store anagrams
    
    # Loop through the array of words to autocorrect and create an array of length 26 to store count of characters in each word
    for word in queries:
        char_count = [0] * 26
        d = {}
        
        # Going through every character in the word and storing in a hashmap
        for c in word:
            char_count[ord(c) - ord('a')] += 1
        d[tuple(char_count)] = []
        
        
        # Loop through the aray of correct words and add them as anagrams of words in the hashmap
        for w in words:
            c_count = [0] * 26
            for a in w:
                c_count[ord(a) - ord('a')] += 1
            
            # Map each word to autocorrect to their correct words (anagrams)
            if tuple(c_count) in d:
                d[(tuple(char_count))] += [w]
            
        result.append(d.values())
        
    return result
                
            
if __name__ =='__main__':
    queries = ["mites", "brake"]
    words = ["emits", "items", "baker", "times", "break", "cart"]
    
    print(autoCorrect2(words, queries)) 
                