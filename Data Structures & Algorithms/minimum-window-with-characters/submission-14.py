class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tmap = Counter(t)
        need = len(tmap)
        have = 0
        window = defaultdict(int)
        l, r = 0, 0
        res = ""
        resLen = float('inf')
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in tmap and window[s[r]] == tmap[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                window[s[l]] -= 1
                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        return res