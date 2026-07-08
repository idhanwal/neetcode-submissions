class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def func(i, comb, res):
            if i >= len(nums):
                res.add(tuple(comb.copy()))
                return
            
            comb.append(nums[i])
            func(i + 1, comb, res)
            comb.pop()
            func(i + 1, comb, res)
        
        func(0, [], res)
        result = []
        for comb in res:
            result.append(list(comb))
        return result