class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def combinations(i, target, comb, res):
            if target == 0:
                res.add(tuple(comb.copy()))
            
            if i >= len(candidates):
                return
            
            if candidates[i] <= target:
                #pick 
                comb.append(candidates[i])
                combinations(i + 1, target - candidates[i], comb, res)
                #not pick
                comb.pop()
                combinations(i + 1, target, comb, res)
        combinations(0, target, [], res)
        # print(res)
        result = []
        for tup in res:
            result.append(list(tup))
        
        return result

