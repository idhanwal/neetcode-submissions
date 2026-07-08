class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = ""
        for c in s:
            if c.isalnum():
                string += c
        string = string.lower()
        return string == string[::-1]
        
        