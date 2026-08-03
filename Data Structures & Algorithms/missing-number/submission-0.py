class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        print(total)
        for num in nums:
            total -= num
        
        return total