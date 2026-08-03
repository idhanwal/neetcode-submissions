class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def rec(i, comb, total):
            if total == target:
                res.append(comb[::])
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target:
                   break
                comb.append(candidates[j])
                rec(j + 1, comb, total + candidates[j])
                comb.pop()
        
        rec(0, [], 0)
        return res