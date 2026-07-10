class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapper = {}

        for i, num in enumerate(nums):
            if target - num in mapper:
                return [mapper[target-num], i]
            mapper[num] = i
        