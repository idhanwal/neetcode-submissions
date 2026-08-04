class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = list(range(1, n + 1))
        # print(nums)
        def rec(i, comb):
            if len(comb) == k:
                res.append(comb[::])
                return
            if i >= n:
                return
            comb.append(nums[i])
            rec(i + 1, comb)
            comb.pop()
            rec(i + 1, comb)
        rec(0, [])
        return res