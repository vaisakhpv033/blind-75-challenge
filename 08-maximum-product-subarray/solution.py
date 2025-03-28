# link: https://leetcode.com/problems/maximum-product-subarray/
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = float('-inf')
        max_val, min_val = 1, 1
        for i in nums:
            if i == 0:
                max_val, min_val = 1, 1
                if 0 > output:
                    output = 0
                continue
            max_val, min_val = max(max_val * i, min_val * i, i) , min(max_val * i, min_val * i, i)
            if max_val > output:
                output = max_val
        return output
    

# Time Complexity: O(n)
# space Complexity: O(1)