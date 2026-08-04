class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        def rec(i, comb):
            if i >= len(s):
                res.append(" ".join(comb[::]))
                return
            
            for j in range(i, len(s)):
                w = s[i:j + 1]
                if w in wordDict:
                    comb.append(w)
                    rec(j + 1, comb)
                    comb.pop()
        
        rec(0, [])
        return res
            