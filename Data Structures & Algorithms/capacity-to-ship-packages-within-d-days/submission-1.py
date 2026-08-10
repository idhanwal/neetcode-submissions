class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        res = 0
        while low <= high:
            mid = (low + high) // 2
            curr = 0
            d = 1
            for w in weights:
                if w + curr <= mid:
                    curr += w
                else:
                    d += 1
                    curr = w
            print(mid, d)
            if d > days:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res

