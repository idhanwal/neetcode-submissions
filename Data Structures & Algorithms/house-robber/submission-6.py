class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)  
        # memo = [-1] * (n + 1)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if memo[i] != -1:
        #         return memo[i]
        #     memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
        #     return memo[i]
        
        # return max(dfs(0), dfs(1))

        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1] , nums[i] + dp[i - 2])
        
        return dp[-1]