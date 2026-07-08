class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = set()
        seen.add(nums[0])

        for j in range(1, len(nums)):
            if target - nums[j] in seen:
                num = target - nums[j]
                numIdx = nums[0: j].index(num)
                return [numIdx, j]
            seen.add(nums[j])