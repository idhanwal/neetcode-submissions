class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charDict = {}

        for ch in s:
            if ch in charDict:
                charDict[ch] += 1
            else:
                charDict[ch] = 1
        
        for ch in t:
            if ch in charDict and charDict[ch] > 0:
                charDict[ch] -= 1
            else:
                return False
        return True
        