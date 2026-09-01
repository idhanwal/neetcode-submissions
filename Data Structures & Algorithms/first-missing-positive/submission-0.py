class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)

        s = 1
        while s in num_set:
            s += 1
        return s