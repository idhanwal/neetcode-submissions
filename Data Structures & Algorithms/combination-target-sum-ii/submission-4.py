class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def dfs(i, nums, total):
            if total == target:
                res.add(tuple(nums))
                return
            if total > target or i == len(candidates):
                return
            
            nums.append(candidates[i])
            dfs(i + 1, nums, total + candidates[i])
            nums.pop()
            dfs(i + 1, nums, total)

        dfs(0, [], 0)
        return [list(tup) for tup in res]
