class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        for i in range(0, len(s)):
            newstr = ""
            j = i
            while j < len(s):
                if s[j] not in newstr:
                    newstr += s[j]
                else:
                    break
                print(newstr)
                j += 1
            maxL = max(maxL, len(newstr))
        return maxL


        
        