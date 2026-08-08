class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s == s[::-1]:
            return True
        

        for i in range(len(s)):
            newString = s[:i] + s[i + 1:]
            if newString == newString[::-1]:
                return True
        
        return False