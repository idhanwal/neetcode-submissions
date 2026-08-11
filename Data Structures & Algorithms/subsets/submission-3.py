class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def get_subsets(i, sub):
            if i >= len(nums):
                res.append(sub[::])
                return
            
            #pick
            sub.append(nums[i])
            get_subsets(i + 1, sub)
            #not pick
            sub.pop()
            get_subsets(i + 1, sub)
        
        get_subsets(0, [])
        return res
        