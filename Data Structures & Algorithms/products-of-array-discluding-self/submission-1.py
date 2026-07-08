class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        print(res)
        n = 1
        for i in range(len(nums)):
            res[i] = n
            n *= nums[i]
            print(res)
            
        n = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] = res[i] * n
            n *= nums[i]
            print(res)
        
        return res
        