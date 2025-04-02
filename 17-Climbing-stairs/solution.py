# link: https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(n):
            if n == 0:
                return 1
            if n in cache:
                return cache[n]
            total = climb(n-1) + (climb(n-2) if n-2 >= 0 else 0)
            cache[n] = total
            return total
        return climb(n)
    
# time complexity: O(n)
# space complexity: O(n)