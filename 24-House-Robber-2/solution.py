# link: https://leetcode.com/problems/house-robber-ii/
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def cash(idx, flag=False):
            if idx >= len(nums):
                return 0
            if idx == len(nums) - 1 and flag:
                return 0 
            if (idx, flag) in cache:
                return cache[(idx, flag)]

            taken = nums[idx] + (cash(idx+2, flag=True) if idx == 0 else cash(idx+2, flag=flag))
            not_taken = cash(idx+1, flag=flag)

            cache[(idx, flag)] = max(taken, not_taken)
            return cache[(idx, flag)]
        
        return cash(0)

# time complexity: O(n)
# space complexity: O(n)
# n is the length of nums