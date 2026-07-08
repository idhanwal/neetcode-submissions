class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0, len(nums)):
            diff = target - nums[i]
            j = 0
            while j < len(nums):
                if nums[j] == diff and j != i:
                    return [i, j]
                j += 1



        