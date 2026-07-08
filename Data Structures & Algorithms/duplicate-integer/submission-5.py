class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        # numSet.add(nums[0])
        for i in range(0, len(nums)):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
        return False