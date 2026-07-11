class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tmap = Counter(t)
        need = len(t)
        have = 0
        l, r = 0, 0

        window = defaultdict(int)
        res = float('inf')
        ans = ""
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in tmap and window[c] <= tmap[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < res:
                    ans = s[l : r + 1]
                    res = r - l + 1
                c = s[l]
                window[c] -= 1
                if c in tmap and window[c] < tmap[c]:
                    have -= 1
                l += 1
        return ans
