class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s.lowercase()
        lower = s.lower()
        f = ""

        for c in lower:
            if c.isalnum():
                f += c
        print(f)
        l, r = 0, len(f) - 1
        while l <= r:
            if f[l] != f[r]:
                return False
            l += 1
            r -= 1
        return True