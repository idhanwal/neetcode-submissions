class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = 0
        while low <= high:
            mid = (high + low) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            print(mid, hours)
            if hours > h:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res

        
