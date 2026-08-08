class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        numset = set()
        k = - 1
        i = 0

        while i < len(nums):
            if nums[i] not in numset:
                numset.add(nums[i])
                k += 1
                nums[k] = nums[i]
            i += 1
        
        return k + 1