"""
Problem: Signal Filter / Filter Ranges

You are given an array of integers `values` (signals) and a list of filter
ranges, where each range is [lowerBound, upperBound].

Each filter range acts like a bandpass filter — only signals that fall within
ALL of the given filter ranges simultaneously should pass through (like a funnel).

Return the count of values that lie within the intersection of all filter
ranges (inclusive on both ends).

Example:
    values       = [1, 3, 5, 7, 9, 11]
    filterRanges = [[2, 10], [4, 8], [3, 9]]

    Intersection = [max(2,4,3), min(10,8,9)] = [4, 8]
    Values in [4, 8]: 5, 7  →  return 2

Constraints:
    - If the filter ranges do not overlap at all (lower > upper after
      intersection), no values can pass through, so return 0.

Time Complexity:  O(R + N) where R = number of ranges, N = len(values)
Space Complexity: O(1)
"""

from typing import List


def filter_ranges(values: List[int], ranges: List[List[int]]) -> int:
    """
        Return the count of values that lie within the intersection of all filter
        ranges (inclusive on both ends).    
        
        Intuition:
            - The intersection of all filter ranges can be found by taking the
              maximum of the lower bounds and the minimum of the upper bounds.
            - Once we have the intersection range, we can count how many values
              fall within that range.   
              
        Steps:
            1. Initialize lower_boundary to -inf and upper_boundary to +inf.
            2. Iterate through each filter range:
                - Update lower_boundary to be the maximum of itself and the current range's lower bound.
                - Update upper_boundary to be the minimum of itself and the current range's upper bound.
            3. After processing all ranges, lower_boundary and upper_boundary will define the intersection range.
            4. Iterate through the values and count how many fall within [lower_boundary, upper_boundary].
            5. Return the count.
            6. If the ranges do not overlap (lower_boundary > upper_boundary), return 0.
        
        Time Complexity: O(R + N) where R = number of ranges, N = len(values)
        Space Complexity: O(1)
    """
    # Phase 1: Find the intersection of all filter ranges.
    # Tighten the window by taking the highest lower bound
    # and the lowest upper bound across every range.
    lower_boundary = float("-inf")
    upper_boundary = float("inf")

    for lower_range, high_range in ranges:
        if lower_boundary < lower_range:
            lower_boundary = lower_range
        if upper_boundary >= high_range:
            upper_boundary = high_range

    print(f"LowerBoundary: {lower_boundary}  UpperBoundary: {upper_boundary}")

    # Phase 2: Count values that survive the funnel (fall within the window).
    result = 0
    for value in values:
        if lower_boundary <= value <= upper_boundary:
            result += 1

    return result

def filter_ranges2(values: List[int], ranges: List[List[int]]) -> int:
    """Return the count of values that lie within the intersection of all filter
    ranges (inclusive on both ends).    
    
    Intuition:
        - The intersection of all filter ranges can be found by taking the
          maximum of the lower bounds and the minimum of the upper bounds.
        - Once we have the intersection range, we can count how many values
          fall within that range.   
          
    Steps:
        1. Initialize start to -inf and end to +inf.
        2. Iterate through each filter range:
            - Update start to be the maximum of itself and the current range's lower bound.
            - Update end to be the minimum of itself and the current range's upper bound.
        3. After processing all ranges, start and end will define the intersection range.
        4. If start > end, it means the ranges do not overlap, so return 0.
        5. Iterate through the values and count how many fall within [start, end].
        6. Return the count.    
        
    Time Complexity: O(R + N) where R = number of ranges, N = len(values)
    Space Complexity: O(1)
    """
    
    start = float("-inf") # Start with the lowest possible value for the lower boundary
    end = float('inf') # Start with the highest possible value for the upper boundary
    
    for start_range, end_range in ranges:
        start = max(start, start_range) # Update start to be the maximum of itself and the current range's lower bound
        end = min(end, end_range) # Update end to be the minimum of itself and the current range's upper bound
        
    if start > end: # If the ranges do not overlap, return 0
        return 0
    
    count = 0
    for value in values:
        if start <= value <= end: # Check if the value falls within the intersection range
            count += 1
            
    return count

def filter_ranges_optimized(values: List[int], ranges: List[List[int]]) -> int:
    """Optimized version of filter_ranges using binary search.
    
        Intuition:
            - We first find the intersection range [start, end] of all filter ranges.
            - Then, we use binary search to quickly count how many values fall within this range.

        Steps:
            1. Find the left index (inclusive) using binary search.
            2. Find the right index (exclusive) using binary search.
            3. The count of values within the range is right_index - left_index.    
            4. If the ranges do not overlap (start > end), return 0.    
            5. Return the count.
        
        Time Complexity: O(R + log N) where R = number of ranges, N = len(values)
        Space Complexity: O(1)
    """
    
    start = float("-inf")
    end = float('inf')
    
    for start_range, end_range in ranges:
        start = max(start, start_range)
        end = min(end, end_range)
        
    if start > end:
        return 0

    # Use binary search to find the count of values within [start, end]
    # Find the left index (inclusive)
    l, r = 0, len(values) - 1
    while l <= r:
        mid = (l + r) // 2
        if values[mid] < start:
            l = mid + 1
        else:
            r = mid - 1
    left_index = l

    # Find the right index (exclusive)
    l, r = 0, len(values) - 1
    while l <= r:
        mid = (l + r) // 2
        if values[mid] <= end:
            l = mid + 1
        else:
            r = mid - 1
    right_index = l

    return right_index - left_index 

# ── Tests ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    for func in [filter_ranges, filter_ranges2, filter_ranges_optimized]:
        # Basic case: intersection is [4, 8], values 5 and 7 survive
        assert func([1, 3, 5, 7, 9, 11], [[2, 10], [4, 8], [3, 9]]) == 2

        # Single range: acts as a simple window filter
        assert func([1, 2, 3, 4, 5], [[2, 4]]) == 3

        # All values pass (wide range)
        assert func([1, 2, 3], [[0, 10]]) == 3

        # No values pass (ranges don't overlap — lower > upper)
        assert func([1, 2, 3, 4, 5], [[1, 3], [4, 6]]) == 0

        # Boundary values are inclusive
        assert func([2, 5, 8], [[2, 8], [2, 8]]) == 3

    print("All tests passed!")
