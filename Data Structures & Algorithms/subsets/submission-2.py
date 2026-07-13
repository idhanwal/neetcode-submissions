class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(i, comb):
            if i == len(nums):
                res.append(comb[:])
                return
            
            comb.append(nums[i])
            rec(i + 1, comb)
            comb.remove(nums[i])
            rec(i + 1, comb)
        
        rec(0, [])
        return res