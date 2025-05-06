# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        count = 0
        maximum = 0
        start_idx = 0
        for idx, val in enumerate(s):
            if val not in cache:
                count += 1
                cache[val] = idx
            else:
                if count > maximum:
                    maximum = count 
                count = idx - cache[val]
                for i in range(start_idx, cache[val]):
                    del cache[s[i]]
                start_idx = cache[val] + 1
                cache[val] = idx
        return maximum if maximum > count else count
# time complexity: O(n)
# space complexity: O(n)