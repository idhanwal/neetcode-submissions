class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        def rec(i, comb, s):
            if s == 0:
                res.append(comb[:])
                return
            
            for x in range(i, len(candidates)):
                if x > i and candidates[x] == candidates[x - 1]:
                    continue
                if s - candidates[x] < 0:
                    break
                
                comb.append(candidates[x])
                rec(x + 1, comb, s - candidates[x])
                comb.pop()
        
        rec(0, [], target)
        return res