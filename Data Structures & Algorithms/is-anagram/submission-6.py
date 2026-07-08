class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charDict = {}
        for ch in s:
            if ch in charDict:
                charDict[ch] = charDict[ch] + 1
            else:
                charDict[ch] = 1
        print(charDict)
        for ch in t:
            if ch in charDict:
                charDict[ch] = charDict[ch] - 1
            else:
                return False
        for key in charDict.keys():
            if charDict[key] != 0:
                return False
        return True

        