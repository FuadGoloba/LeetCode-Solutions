# Insert Interval

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval 
# and intervals is sorted in ascending order by starting. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

def insertInterval(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    '''
        Time Complexity = O(n)
        Space Complexity = O(1)
        
        Note: To insert an interval into a sorted list of intervals, we need to check 3 corner cases
            An overlap occurs when values of 2 intervals that can be merged into one interval are coinciding with one another. eg [2, 7], [1, 5] are overlapping and can be merged into [1, 7]
            i. when the newInterval to be inserted has values lower than the current interval in the intervals list; insert before the current interval if it's not overlapping
            ii. when the newInterval to be inserted has values higher than the current interval in the intervals list; insert after the current interval if it's not overlapping
            iii. when the newInterval is overlapping with intervals in the intervals list; merge overlapping intervals before inserting
    '''
    output = []
    for idx in range(len(intervals)):
        # case 1; insert before the current interval if newInterval is lower
        if newInterval[1] < intervals[idx][0]:
            output.append(newInterval)
            return output + intervals[idx:]
        # case 2: insert after the current interval is newInterval is higher
        elif newInterval[0] > intervals[idx][1]:
            output.append(intervals[idx])
        # case 3: merge overlapping intervals and continue until there are no overlaps with the next interval in the interval list
        else:
            lower = min(newInterval[0], intervals[idx][0])
            upper = max(newInterval[1], intervals[idx][1])
            newInterval = [lower, upper]
    output.append(newInterval)
    return output

if __name__ == '__main__':
    inputs = [
        ([[1,3],[6,9]], [2,5]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
    ]  
    for intervals, newInterval in inputs:
        print(insertInterval(intervals, newInterval))
    
        
            
        
    