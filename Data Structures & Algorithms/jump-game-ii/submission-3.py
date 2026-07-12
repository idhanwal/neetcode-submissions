class Solution:
    def jump(self, nums: List[int]) -> int:
        # memo = {}
        # def dfs(i):
        #     if i >= len(nums) - 1:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     min_jumps = float('inf')
        #     for j in range(1, nums[i] + 1):
        #         min_jumps = min(min_jumps, 1 + dfs(i + j))
        #     memo[i] = min_jumps
        #     return memo[i]
        
        # return dfs(0)
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l , r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
        