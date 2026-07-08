class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        map = dict.fromkeys(nums, False)
        def perm(i, map, comb, res):
            if i >= len(nums):
                res.append(comb.copy())
                return

            for k in map.keys():
                if not map[k]:
                    comb.append(k)
                    map[k] = True
                    perm(i + 1, map, comb, res)
                    comb.pop()
                    map[k] = False
        perm(0, map, [], res)
        return res
        
