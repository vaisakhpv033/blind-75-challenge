# link: https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache_array = [[None for j in range(len(text2))] for i in range(len(text1))]        
        def LCS(i, j):
            if i == len(text1) or j == len(text2):
                return 0 

            if cache_array[i][j] is not None:
                return cache_array[i][j]

            if text1[i] == text2[j]:
                cache_array[i][j] = 1 + LCS(i+1, j+1)
                return cache_array[i][j]
            else:
                cache_array[i][j] = max(LCS(i+1, j), LCS(i, j+1))
                return cache_array[i][j]

        return LCS(0, 0)
    
# time complexity: O(m*n)
# space complexity: O(m*n)
# m = len(text1)
# n = len(text2)
# where m and n are the lengths of the two strings