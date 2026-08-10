class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # memo = {}
        # def rec(i, j):
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
            
        #     if (i, j) not in memo:
        #         memo[(i, j)] = 0
        #         if text1[i] == text2[j]:
        #             memo[(i, j)] = 1 + rec(i + 1, j + 1)
        #         else:
        #             memo[(i, j)] = max(rec(i + 1, j), rec(i, j + 1))
            
        #     return memo[(i, j)]
        
        # res = rec(0, 0)
        # return res
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]




