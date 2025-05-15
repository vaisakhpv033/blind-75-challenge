# link: https://neetcode.io/problems/string-encode-and-decode
class Solution:
    def encode(self, strs: List[str]) -> str:
        new_val = []
        for val in strs:
            new_val.append(f"{len(val)}#{val}")
        return "".join(new_val)

    def decode(self, s: str) -> List[str]:
        output = []
        count = "0"
        idx = 0
        while idx < len(s):
            val = s[idx]
            
            if val == "#":
                end = idx + int(count) + 1
                output.append(s[idx+1:end])
                count = "0"
                idx = end
            else:
                count += s[idx]
                idx += 1
        return output 
            

