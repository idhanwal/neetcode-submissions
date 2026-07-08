class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        length = len(s)

        for i in range(0, length):
            j = i
            k = j
            while j > -1 and k < length and s[j] == s[k]:
                count += 1
                j -= 1
                k += 1
            
            j = i
            k = j + 1

            while j > -1 and k < length and s[j] == s[k]:
                count += 1
                j -= 1
                k += 1
        
        return count

        