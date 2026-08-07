class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mapper = Counter(nums)

        for key in mapper:
            if mapper[key] >= len(nums) // 2:
                return key