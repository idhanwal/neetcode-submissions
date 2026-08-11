class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def rec(i, total, comb):
            if total == target:
                res.append(comb[::])
                return
            if i >= len(nums) or total > target:
                return
            if nums[i] + total  <= target:
                comb.append(nums[i])
                rec(i, total + nums[i], comb)
                comb.pop()
            rec(i + 1, total, comb)
        rec(0, 0, [])
        return res