class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        print(numset)
        res = 0
        for num in nums:
            print(num)
            count = 1
            n = num - 1
            while n in numset:
                count += 1
                n -=  1
            n = num + 1
            while n in numset:
                n += 1
                count += 1
            res = max(res, count)
        return res

