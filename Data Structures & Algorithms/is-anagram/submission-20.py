class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapper = Counter(s)

        for ch in t:
            if ch not in mapper:
                return False
            else:
                mapper[ch] -= 1
                if mapper[ch] == 0: del mapper[ch]

        return True if not mapper else False