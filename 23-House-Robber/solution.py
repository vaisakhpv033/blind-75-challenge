# link: https://leetcode.com/problems/house-robber/description/
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def cash(idx):
            if idx >= len(nums):
                return 0
            if idx in cache:
                return cache[idx]
            taken = nums[idx] + cash(idx+2)
            not_taken = cash(idx+1)
            cache[idx] = max(taken, not_taken)
            return cache[idx]
        
        return cash(0)

# time complexity: O(n)
# space complexity: O(n)
# n is the length of nums