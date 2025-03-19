# Link: https://leetcode.com/problems/two-sum/
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, val in enumerate(nums):
            value = target - val
            if value in cache:
                return [cache[value], idx]
            cache[val] = idx