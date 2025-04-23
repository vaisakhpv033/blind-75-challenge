# link: https://leetcode.com/problems/non-overlapping-intervals/
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        count = 0
        interval = intervals[0]
        for idx in range(1, len(intervals)):
            if intervals[idx][0] < interval[1]:
                count += 1
                interval = interval if intervals[idx][1] > interval[1] else intervals[idx]
            else:
                interval = intervals[idx]

        return count
    
# time complexity: O(nlogn)
# space complexity: O(n)