class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        result = []
        for i in range(0, len(nums)):
            result.append(prod)
            prod = nums[i] * prod
        print(result)
        prod = 1
        for i in range(len(nums) - 1, -1, - 1):
            result[i] = result[i] * prod
            prod = prod * nums[i]
        
        return result
        