#link: https://leetcode.com/problems/maximum-subarray/
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref_sum = 0
        max_sum = float('-inf')
        for i in nums:
            if pref_sum < 0:
                pref_sum = 0
            pref_sum += i
            if pref_sum > max_sum:
                max_sum = pref_sum
        return max_sum
    
# Time complexity: O(n)
# Space complexity: O(1)