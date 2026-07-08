class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numSet = set()
        numSet.add(nums[0])

        for j in range(1, len(nums)):
            if target - nums[j] in numSet:
                i = nums[ : j].index(target - nums[j])
                return [i, j]
            else:
                numSet.add(nums[j])