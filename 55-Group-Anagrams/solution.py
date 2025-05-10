# link: https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        dict1 = {}
        for char in strs:
            key = ''.join(sorted(char))
            if key in dict1:
                dict1[key].append(char)
            else:
                dict1[key] = [char,]
        return [val for val in dict1.values()]
    
