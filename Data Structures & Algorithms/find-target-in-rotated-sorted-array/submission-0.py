class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l: int, r: int, nums: List[int], target: int) -> int:
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        result = binary_search(0, pivot - 1, nums, target)
        if result != -1:
            return result
        return binary_search(pivot, len(nums) - 1, nums, target)


        