"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# linK: https://neetcode.io/problems/meeting-schedule
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals = self.mergesort(intervals)
        interval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i].start < interval.end:
                return False
            else:
                interval = intervals[i]
        return True
        
        
    def mergesort(self, array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = self.mergesort(array[:mid])
        right = self.mergesort(array[mid:])
        return self.merge(left, right)

    
    def merge(self, array1, array2):
        merged_array = []
        idx1, idx2 = 0, 0
        while idx1 < len(array1) and idx2 < len(array2):
            if array1[idx1].start < array2[idx2].start:
                merged_array.append(array1[idx1])
                idx1 += 1
            else:
                merged_array.append(array2[idx2])
                idx2 += 1
        
        while idx1 < len(array1):
            merged_array.append(array1[idx1])
            idx1 += 1
        
        while idx2 < len(array2):
            merged_array.append(array2[idx2])
            idx2 += 1
        return merged_array

# time complexity: O(nlogn)
# space complexity: O(n)