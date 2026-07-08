class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ele = set(nums)

        res = 0
        for num in nums:
            length = 1
            while num + 1 in ele:
                num += 1
                length += 1
            res = max(length, res)
        return res
        