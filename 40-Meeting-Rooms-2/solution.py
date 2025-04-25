"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# link: https://neetcode.io/problems/meeting-schedule-ii
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()

        count = 0
        max_days = 0

        idx1, idx2 = 0, 0

        while idx1 < len(start):
            if start[idx1] < end[idx2]:
                count += 1
                idx1 += 1
                if count > max_days:
                    max_days = count 
            else:
                count -= 1
                idx2 += 1
        return max_days

# time complexity: O(nlogn)
# space complexity: O(n)