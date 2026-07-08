class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxL = 0
        # for i in range(0, len(s)):
        #     newstr = ""
        #     j = i
        #     while j < len(s):
        #         if s[j] not in newstr:
        #             newstr += s[j]
        #         else:
        #             break
        #         j += 1
        #     maxL = max(maxL, len(newstr))
        # return maxL

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        
        