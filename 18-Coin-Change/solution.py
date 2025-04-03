# link: https://leetcode.com/problems/coin-change/description/
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def count(n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            
            if n in cache:
                return cache[n]
            
            output = []
            for i in coins:
                value = count(n-i)
                if value == -1:
                    continue
                else:
                    output.append(1 + value)
            if not output:
                cache[n] = -1
                return -1
            else:
                cache[n] = min(output)
                return cache[n]
        return count(amount)

# time complexity: O(n)
# space complexity: O(n)