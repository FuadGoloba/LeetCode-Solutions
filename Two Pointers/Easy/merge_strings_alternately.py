"""
    Merge Strings Alternately

    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
    If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.
    
    Example 1:
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r
    
    Example 2:
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b 
    word2:    p   q   r   s
    merged: a p b q   r   s
    
    Example 3:
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q 
    merged: a p b q c   d
    
    Constraints:
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
    """


def merge_strings_alternately(word1, word2):
    """
    Merges two strings in alternating order.

    Intuition:
        - Use a loop to iterate through both strings simultaneously, appending characters from each string in turn.
        - If one string is longer, append the remaining characters after the loop.

    Time Complexity: O(n), where n is the total length of both input strings.
    Space Complexity: O(n), for the output merged string.

    Steps:
        1. Determine the minimum length of the two strings.
        2. Use a loop to append characters from both strings up to the minimum length.
        3. Append any remaining characters from the longer string after the loop.

    Note: The inefficiency of this approach is that it may involve multiple string concatenations,
        which can be inefficient in Python due to the immutability of strings.
        A more efficient approach would be to use a list to build the merged string and then join it at the end.
    """
    min_length = min(len(word1), len(word2))
    new_string = ""
    for idx in range(min_length):
        new_string += word1[idx] + word2[idx]

    if len(word1) > min_length:
        new_string += word1[min_length::]
    if len(word2) > min_length:
        new_string += word2[min_length::]

    return new_string


def merge_strings_alternately_better(word1, word2):
    """
    Merges two strings in alternating order using Two Pointers and a list to build the merged string.

    Intuition:
        - Use a list to store characters from both strings in alternating order.
        - After the loop, join the list into a single string.

    Time Complexity: O(n), where n is the total length of both input strings.
    Space Complexity: O(n), for the output merged string.

    Steps:
        1. Initialize an empty list to hold the merged characters.
        2. Use two pointers to iterate through both strings simultaneously, appending characters to the list.
        3. After the loop, append any remaining characters from the longer string to the list.
        4. Join the list into a single string and return it.
    """
    merged = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    # Append any remaining characters from either string
    merged.append(word1[i:])
    merged.append(word2[j:])
    return "".join(merged)


def merge_strings_alternately_optimal(word1, word2):
    """
    Merges two strings in alternating order using Two Pointers and a list to build the merged string.

    Intuition:
        - Use a single loop to iterate up to the maximum length of the two strings, appending characters from both strings if the current index is within their lengths.
        - This approach avoids the need for separate loops to handle remaining characters after the main loop.

    Time Complexity: O(n), where n is the total length of both input strings.
    Space Complexity: O(n), for the output merged string.

    Steps:
        1. Initialize an empty list to hold the merged characters.
        2. Use a single loop to iterate up to the maximum length of the two strings, appending characters from both strings if the current index is within their lengths.
        3. Join the list into a single string and return it.

    """
    merged = []
    len1, len2 = len(word1), len(word2)
    max_len = max(len1, len2)

    for i in range(max_len):
        if i < len1:
            merged.append(word1[i])
        if i < len2:
            merged.append(word2[i])

    return "".join(merged)


if __name__ == "__main__":
    test_cases = [
        ("abc", "pqr"),
        ("ab", "pqrs"),
        ("abcd", "pq"),
        ("", "pqrs"),
        ("abcd", ""),
    ]

    for case in test_cases:
        word1, word2 = case
        print(f"Input: {case} -> Output: {merge_strings_alternately(word1, word2)}")
