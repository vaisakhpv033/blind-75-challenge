# link: https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        chars = {chr(i) for i in range(ord('a'), ord('z')+1)}
        nums = {str(i) for i in range(0, 10)}
        while start <= end:
            if s[start].lower() not in chars and s[start].lower() not in nums:
                start += 1
                continue
            if s[end].lower() not in chars and s[end].lower() not in nums:
                end -= 1
                continue 
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True 
            