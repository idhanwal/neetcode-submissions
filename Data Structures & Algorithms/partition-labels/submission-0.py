class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        ans = []

        for i, c in enumerate(s):
            last[c] = i
        
        track = set()
        l = 0
        for i in range(0, len(s)):
            c = s[i]
            track.add(c)
            if i == last[c]:
                track.remove(c)
            
            if len(track) == 0:
                ans.append(i - l + 1)
                l = i + 1
        return ans
