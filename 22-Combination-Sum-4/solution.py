# link: https://leetcode.com/problems/combination-sum-iv/description/
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        def combination(value):
            if value == 0:
                return 1
            elif value < 0:
                return 0
            if value in cache:
                return cache[value]
            count = 0
            for i in nums:
                count += combination(value-i)
            cache[value] = count
            return cache[value]
        return combination(target)

# time complexity: O(n * target)
# space complexity: O(target)
# n is the length of nums