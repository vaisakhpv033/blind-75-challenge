# link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)  - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[end]:
                if target > nums[mid]:
                    start = mid + 1
                else:
                    if target < nums[start]:
                        start = mid + 1
                    else:
                        end = mid - 1
            else:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    if target > nums[end]:
                        end = mid - 1
                    else:
                        start = mid + 1
        return -1

# Time complexity: O(logn)
# Space complexity: O(1)