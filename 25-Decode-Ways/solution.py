# link: https://leetcode.com/problems/decode-ways/description/
class Solution:
    def numDecodings(self, s: str) -> int:
        decode_keys = {f"{i+1}" for i in range(26)}
        cache = {}

        def values(s):
            if len(s) <=1:
                if s == "0":
                    return 0
                return 1
            if s in cache:
                return cache[s]
            total1 = 0
            if s[:1] in decode_keys:
                total1 = values(s[1:])
            total2 = 0
            if s[:2] in decode_keys and len(s) >= 2:
                total2 = values(s[2:])
            cache[s] = total1 + total2
            return cache[s]
        
        return values(s)
    
# time complexity: O(n)
# space complexity: O(n)
# n is the length of s