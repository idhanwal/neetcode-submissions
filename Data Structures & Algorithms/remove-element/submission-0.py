class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = -1
        i = 0
        while i < len(nums):
            if nums[i] != val:
                k += 1
                nums[k] = nums[i] 
            i += 1
        
        return k + 1