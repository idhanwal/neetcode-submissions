class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dest = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= dest:
                dest = i
            if dest == 0:
                return True
        return False