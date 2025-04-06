# link: https://leetcode.com/problems/word-break/description/
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp_array = [False for i in range(len(s)+1)]
        dp_array[0] = True 
        max_len = 0
        wordDict = set(wordDict)
        for i in wordDict:
            if len(i) > max_len:
                max_len = len(i)
        for idx, _ in enumerate(s):

            for j in range(idx, -1, -1):
                if idx - j >= max_len:
                    break
                
                if s[j:idx+1] in wordDict:
                    if dp_array[j] is True:
                        dp_array[idx+1] = True
                        break
        return dp_array[-1]
    
# time complexity: O(n^2)
# space complexity: O(n)