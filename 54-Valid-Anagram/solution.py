# link: https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {} 
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        
        for i in t:
            if i not in dict1 or dict1[i] == 0:
                return False 
            dict1[i] -= 1
        return True