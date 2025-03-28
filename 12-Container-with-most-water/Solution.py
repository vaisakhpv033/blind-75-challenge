# link: https://leetcode.com/problems/container-with-most-water/
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        maximum = 0
        while start < end:
            value = min(height[start], height[end]) * (end - start)
            if value > maximum:
                maximum = value
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return maximum

# time complexity: O(n)
# space complexity: O(1)