class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            heapq.heappush(heap, (abs(x - num), num))
        res = []
        while heap:
            dist, num = heapq.heappop(heap)
            res.append(num)
            if len(res) == k:
                res.sort()
                return res
    