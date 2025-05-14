# link: https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0
        for i in range(len(s)):
            start, end = i-1, i+1
            count = 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
            
            start, end = i, i+1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
            total_count += count
        return total_count
            