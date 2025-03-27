from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cache = set()
        output = set()
        for idx, val in enumerate(nums):
            if idx and nums[idx-1] == nums[idx]:
                continue
            if val >0:
                break
            for i in range(idx+1, len(nums)):
                value = -val - nums[i]
                if value in cache:
                    output.add((val, nums[i], value))
                    cache.remove(value)
                    continue
                cache.add(nums[i])
            cache = set()
        return [list(i) for i in output]
