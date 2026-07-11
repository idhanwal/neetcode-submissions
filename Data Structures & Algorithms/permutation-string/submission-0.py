class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map = Counter(s1)

        n = len(s1)

        window = defaultdict(int)

        l, r = 0, 0

        for r in range(len(s2)):
            window[s2[r]] += 1
            if r >= n:
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            if window == s1map:
                return True
        
        return False