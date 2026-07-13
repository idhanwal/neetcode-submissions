class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = (r + l) // 2 
            j = 0
            time = sum((p + k - 1) // k for p in piles)
            if time > h:
                l = k + 1
            else:
                res = k
                r = k - 1

        return res

