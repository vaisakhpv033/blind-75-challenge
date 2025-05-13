# link: https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        max_count = 0
        for i in range(len(s)):
            left, right = i-1, i+1
            count = 1
            st, en = i, i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 2
                    st, en = left, right
                else:
                    break
                left -= 1
                right += 1
            if count > max_count:
                max_count = count
                result = s[st:en+1]
            left, right = i, i+1
            count = 0
            st, en = left, right
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    count += 2
                    st, en = left, right
                else:
                    break
                left -= 1
                right += 1
            if count > max_count:
                max_count = count
                result = s[st:en+1]
        return result 
