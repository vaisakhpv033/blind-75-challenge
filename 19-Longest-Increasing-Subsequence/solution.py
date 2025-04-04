# link: https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp_array = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp_array[j] + 1 > dp_array[i]:
                        dp_array[i] = dp_array[j] + 1
            
        return max(dp_array)
    
# time complexity: O(n^2)
# space complexity: O(n)