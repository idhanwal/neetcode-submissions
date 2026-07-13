class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def rec(i, comb):
            if i == len(nums):
                res.add(tuple(comb[:]))
                return
            
            comb.append(nums[i])
            rec(i + 1, comb)
            comb.pop()
            rec(i + 1, comb)
        
        rec(0, [])
        return [list(tup) for tup in res]
                