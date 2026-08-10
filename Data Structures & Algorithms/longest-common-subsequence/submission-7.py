class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        def rec(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) not in memo:
                memo[(i, j)] = 0
                if text1[i] == text2[j]:
                    memo[(i, j)] = 1 + rec(i + 1, j + 1)
                else:
                    memo[(i, j)] = max(rec(i + 1, j), rec(i, j + 1))
            
            return memo[(i, j)]
        
        res = rec(0, 0)
        return res


