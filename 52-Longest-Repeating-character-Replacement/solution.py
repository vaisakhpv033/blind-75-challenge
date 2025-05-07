# link: https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp=defaultdict(int)
        l=sm=res=0
        for r in range(len(s)):
            mp[s[r]]+=1

            while (r-l+1) - max(mp.values())>k:
                mp[s[l]]-=1
                l+=1
            
            res=max(res,r-l+1)
        return res

        