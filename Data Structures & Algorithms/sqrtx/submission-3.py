class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while l <= r:
            m = (r + l) // 2

            sqr = m * m
            if sqr > x:
                r = m - 1
            elif sqr < x:
                res = m
                l = m + 1
            else:
                return m
        return res