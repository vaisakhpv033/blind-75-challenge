# link: https://leetcode.com/problems/insert-interval/description/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = [] 

        for idx, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[idx:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            if idx == len(intervals) - 1:
                res.append(newInterval)
        return res

# time complexity: O(n)
# space complexity: O(n)