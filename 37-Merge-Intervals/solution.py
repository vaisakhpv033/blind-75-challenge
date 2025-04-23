# link: https://leetcode.com/problems/merge-intervals/description/
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        res = [] 
        new_interval = intervals[0]
        for idx in range(1, len(intervals)):
            if new_interval[1] < intervals[idx][0]:
                res.append(new_interval)
                new_interval = intervals[idx]
            else:
                new_interval = [min(new_interval[0], intervals[idx][0]), max(new_interval[1], intervals[idx][1])]

        res.append(new_interval)
        return res 
    

# time complexity: O(NlogN)
# space complexity: O(N)

