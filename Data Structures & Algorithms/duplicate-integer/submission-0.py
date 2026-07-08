class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ele = set()

        for num in nums:
            if num in ele:
                return True
            ele.add(num)
        return False
         