# link: https://leetcode.com/problems/jump-game/
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def jump(idx):
            if idx == len(nums) - 1:
                return True
            if nums[idx] == 0:
                return False
            if idx >= len(nums):
                return False 

            if idx in cache:
                return cache[idx]


            is_possible = False

            for i in range(1, nums[idx]+1):
                if idx + i in cache:
                    is_possible = cache[idx+i]
                else:
                    is_possible = jump(idx + i)
                    cache[idx + i] = is_possible
                if is_possible:
                    break
            cache[idx] = is_possible
            return cache[idx]
        return jump(0)

# time complexity: O(n)
# space complexity: O(n)
# n is the length of the nums array