class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        # i = 0
        maxLen = 0

        for i in range(len(s)):
            seen.add(s[i])
            j = i + 1
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
            maxLen = max(maxLen, len(seen))
            # i = j
            # print(s[i])
            seen = set()
        
        return maxLen