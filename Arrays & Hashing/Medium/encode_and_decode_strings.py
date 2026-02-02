""" 
    Encode and Decode Strings

    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
    Implement the encode and decode methods.

    Example 1:
    Input: dummy_input = ["Hello","World"]
    Output: ["Hello","World"]
    
    Example 2:
    Input: dummy_input = [""]
    Output: [""]

    Constraints:
    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains any possible characters out of 256 valid ASCII characters.
"""

def encode(strs: list[str]) -> str:
    """
    Encodes a list of strings to a single string for network transmission.
    
    Intuition:
        For each string in the list, prepend its length and a delimiter (e.g., '#'), then concatenate all such segments.
        This allows the decoder to know exactly how many characters to read for each string, even if the string contains the delimiter itself.
    
    Time Complexity: O(N), where N is the total number of characters in all strings in the input list.
    Space Complexity: O(N), for the output encoded string.
    
    Steps:
        1. Initialize an empty string to hold the encoded result.
        2. For each string in the input list:
            - Calculate its length.
            - Append the length, a delimiter '#', ("length#string") and the string itself to the encoded result.
        3. Return the final encoded string.
    """
    
    encoded_str = ''
    for s in strs:
        # Append the length of the string, a delimiter, and the string itself
        encoded_str += str(len(s)) + '#' + s
    return encoded_str

def decode(s: str) -> list[str]:
    """
    Decodes a single string back into a list of strings as encoded by the encode function.
    
    Intuition:
        Iteratively parse the encoded string by reading the length prefix (up to the delimiter '#'),
        then extract the substring of that length, and repeat until the end of the string.
    
    Time Complexity: O(N), where N is the length of the encoded string.
    Space Complexity: O(N), for the output list of strings.
    
    Steps:
        1. Initialize an empty result list and a pointer (curr_idx) at the start of the string.
        2. While the pointer is less than the length of the string:
            - Find the next delimiter '#' to determine the length prefix.
            - Convert the substring before '#' to an integer (word_length).
            - Extract the substring of length word_length after the delimiter and append to the result list.
            - Move the pointer forward by the length of the prefix, delimiter, and word to continue decoding the next segment
        3. Return the result list containing all decoded strings.
    """
    
    res, curr_idx = [], 0
    
    while curr_idx < len(s):
        delimiter_idx  = curr_idx
        # Find the position of the next delimiter '#'
        while s[delimiter_idx] != '#':
            delimiter_idx += 1
        # Extract the length of the next word
        word_length = int(s[curr_idx : delimiter_idx])
        start_word_idx = delimiter_idx + 1
        # Extract the word of the given length and append to result
        res.append(s[start_word_idx : start_word_idx + word_length])
        # Move the pointer to the start of the next encoded word
        curr_idx = start_word_idx + word_length
    return res

if __name__ == '__main__':
    test_cases = [
        ["Hello", "World"],
        [""],
        ["a", "b", "c"],
        ["abc", "defg", "h"],
        [],
        ["#", "##", "###"],
        ["123", "", "!@#"]
    ]
    for case in test_cases:
        encoded = encode(case)
        decoded = decode(encoded)
        # Print the original, encoded, and decoded values for each test case
        print(f"Original: {case}\nEncoded: {encoded}\nDecoded: {decoded}\n")
