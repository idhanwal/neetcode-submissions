class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def get_subsets(i, sub, res):
            if i >= len(nums):
                res.append(sub.copy())
                return
            
            #pick
            sub.append(nums[i])
            get_subsets(i + 1, sub, res)
            #not pick
            sub.pop()
            get_subsets(i + 1, sub, res)
        
        get_subsets(0, [], res)
        return res
        