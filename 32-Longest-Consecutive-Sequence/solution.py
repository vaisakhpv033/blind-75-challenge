# link: https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0 
        for val in nums:
            if val - 1 not in nums:
                total = 1
                value = val + 1
                while value  in nums:
                    total += 1
                    value += 1
                if total > count:
                    count = total
        return count
    
# time Complexity: O(n)
# space Complexity: O(n)