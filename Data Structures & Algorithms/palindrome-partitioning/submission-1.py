class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def isPalindrome(a):
            return a == a[::-1]

        def rec(i, part):
            if i >= len(s):
                res.append(part[::])
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i: j + 1]):
                    part.append(s[i : j + 1])
                    rec(j + 1, part)
                    part.pop()
        
        rec(0, [])
        return res