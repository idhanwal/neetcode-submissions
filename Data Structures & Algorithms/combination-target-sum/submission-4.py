class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def rec(i, comb, s):
            if s == 0:
                res.append(comb[:])
                return
            if i == len(nums):
                return
            
            if s - nums[i] >= 0:
                comb.append(nums[i])
                rec(i, comb, s - nums[i])
                comb.pop()
            rec(i + 1, comb, s)

        rec(0, [], target)
        return res
