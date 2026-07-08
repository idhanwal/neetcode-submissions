class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def combinations(i, target, comb, res):
            if target == 0:
                res.append(comb.copy())
                return
            if i >= len(nums):
                return
            
            if nums[i] <= target:
                #pick
                comb.append(nums[i])
                combinations(i, target - nums[i], comb, res)
                #not pick
                comb.pop()
                combinations(i + 1, target, comb, res)
        
        combinations(0, target, [], res)
        return res