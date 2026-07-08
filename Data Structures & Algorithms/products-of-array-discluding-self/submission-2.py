class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        n = 1
        for i in range(len(nums)):
            res[i] = n
            n *= nums[i]
            
        n = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] = res[i] * n
            n *= nums[i]

        return res
        