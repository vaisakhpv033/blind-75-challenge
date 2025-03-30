# link:https://leetcode.com/problems/counting-bits/description/
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            count = 0
            while i > 0:
                count += i & 1
                i = i >> 1
            output.append(count)
        return output
