class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        for ch in s:
            if ch in dicts:
                dicts[ch] = dicts[ch] + 1
            else:
                dicts[ch] = 1
        
        dictt = {}
        for ch in t:
            if ch in dictt:
                dictt[ch] += 1
            else:
                dictt[ch] = 1
        
        return dicts == dictt