class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dest = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= dest:
                dest = i
            if dest == 0:
                return True
        return False