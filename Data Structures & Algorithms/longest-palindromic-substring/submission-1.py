class Solution:
    def longestPalindrome(self, s: str) -> str:

        length = 1
        res = s[0]
        for i in range(0 , len(s)):
            j = i
            k = j + 1

            while j > -1 and k < len(s) and s[j] == s[k]:
                if abs(k - j) >= length:
                    length = abs(k - j)
                    res = s[j : k + 1]
                j -= 1
                k += 1
            
            j = i - 1
            k = i + 1

            while j > -1 and k < len(s) and s[j] == s[k]:
                if abs(k - j) >= length:
                    length = abs(k - j)
                    res = s[j : k + 1]
                j -= 1
                k += 1
        return res



        