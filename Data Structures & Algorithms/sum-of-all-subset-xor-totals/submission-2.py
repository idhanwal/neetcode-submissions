class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        def rec(i, comb):
            if i >= len(nums):
                xor = 0
                for num in comb:
                    xor = xor ^ num
                self.res += xor
                return
            comb.append(nums[i])
            rec(i + 1, comb)
            comb.pop()
            rec(i + 1, comb)
        
        rec(0, [])
        return self.res

