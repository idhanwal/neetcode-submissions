class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def rec(i, comb):
            res.append(comb[::])
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                comb.append(nums[j])
                rec(j + 1, comb)
                comb.pop()
        
        rec(0, [])
        return res