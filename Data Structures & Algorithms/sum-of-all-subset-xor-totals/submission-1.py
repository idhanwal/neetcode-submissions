class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.xor = 0

        def rec(i, comb):
            
            if i >= len(nums):
                # print(comb[::])
                sum_xor = 0
                for num in comb[::]:
                    sum_xor = sum_xor ^ num
                # print(sum_xor)
                self.xor += sum_xor
                return
            comb.append(nums[i])
            rec(i + 1, comb)
            comb.pop()
            rec(i + 1, comb)
        
        rec(0, [])
        return self.xor