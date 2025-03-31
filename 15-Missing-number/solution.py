# link: https://leetcode.com/problems/missing-number/description/
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n+1)//2
        current_total = sum(nums)
        return total - current_total
    
# time complexity: O(n)
# space complexity: O(1)