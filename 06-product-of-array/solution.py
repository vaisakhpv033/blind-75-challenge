# Source: https://leetcode.com/problems/product-of-array-except-self/
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]
        mul = 1
        for idx, val in enumerate(nums):
            output[idx] *= mul
            mul *= val

        mul = 1
        for idx in range(len(nums)-1, -1, -1):
            output[idx] *= mul
            mul *= nums[idx]
        return output

# Time complexity: O(n)
# Space complexity: O(1)